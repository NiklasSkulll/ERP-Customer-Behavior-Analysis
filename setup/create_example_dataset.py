"""Create randomized CSV copies of the four documented raw ERP datasets.

The input dataset must already be prepared for conversion: all four CSV files
must use the documented filenames and column sets, consistent order headers,
and input formats matching --delimiter and --decimal-mark.

All rows and table relationships are retained. Dates, statuses, currencies,
item numbers and lookup descriptions remain unchanged. Amounts receive random
replacements, with equal numeric amounts receiving equal replacements; zero,
sign and missingness are preserved. Replacements do not preserve monetary trends.
IDs use SO (orders), CU (customers), R (reasons), or I (industries), followed
by a unique random 12-digit number within each category.

These copies are derived from the input dataset, not fully synthetic or
guaranteed anonymous. Mappings are never exported.
"""

import argparse
from bisect import bisect_right
import csv
from decimal import Decimal, InvalidOperation
from hashlib import sha256
from pathlib import Path
from secrets import SystemRandom
import tempfile


ORDERS = "001_order_header_pos_data.csv"
CUSTOMERS = "002_customer_master_data.csv"
REASONS = "003_order_sddocumentreason_mapping.csv"
INDUSTRIES = "004_customer_industry_mapping.csv"
SCHEMAS = {
    ORDERS: (
        "SALESORDER SALESORDERTYPE OVERALLSDPROCESSSTATUS SDDOCUMENTREASON "
        "OVERALLSDDOCUMENTREJECTIONSTS SALESORDERDATE SOLDTOPARTY TOTALNETAMOUNT "
        "TRANSACTIONCURRENCY SALESORDERITEM"
    ).split(),
    CUSTOMERS: ["CUSTOMER", "INDUSTRY"],
    REASONS: ["SDDOCUMENTREASON", "SDDOCUMENTREASON_TEXT"],
    INDUSTRIES: ["INDUSTRY", "INDUSTRY_TEXT"],
}
ID_DOMAINS = {
    "SALESORDER": "orders",
    "SDDOCUMENTREASON": "reasons",
    "SOLDTOPARTY": "customers",
    "CUSTOMER": "customers",
    "INDUSTRY": "industries",
}
ID_PREFIXES = {"orders": "SO", "customers": "CU", "reasons": "R", "industries": "I"}


def amount_value(value: str, decimal_mark: str) -> Decimal | None:
    """Parse a finite decimal without guessing thousands or missing markers."""
    if value == "":
        return None
    text = value.strip()
    if decimal_mark == ",":
        if "." in text:
            raise ValueError("Amounts must not contain thousands separators.")
        text = text.replace(",", ".")
    elif "," in text:
        raise ValueError("Amounts do not match --decimal-mark.")
    try:
        amount = Decimal(text)
    except InvalidOperation:
        raise ValueError("An amount is not a valid decimal; no output was written.") from None
    if not amount.is_finite():
        raise ValueError("Amounts must be finite decimals or empty fields.")
    return amount


def read_rows(path: Path, delimiter: str, digest=None):
    """Stream only documented fields, rejecting extra columns and malformed rows."""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        def lines():
            for line in stream:
                if digest is not None:
                    digest.update(line.encode("utf-8"))
                yield line

        reader = csv.DictReader(lines(), delimiter=delimiter, strict=True)
        columns = reader.fieldnames
        expected = SCHEMAS[path.name]
        if columns is None or len(columns) != len(expected) or set(columns) != set(expected):
            raise ValueError(f"Unexpected CSV columns in {path.name}; check schema and --delimiter.")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV row in {path.name}.")
            yield row


def choose_numbers(count: int, lower: int, upper: int, excluded: set[int]) -> list[int]:
    """Sample without replacement or retries, excluding original numeric values."""
    blocked = sorted(value for value in excluded if lower <= value <= upper)
    capacity = upper - lower + 1 - len(blocked)
    if count > capacity:
        raise ValueError("Replacement range is too small; increase --max-amount.")
    ranks = SystemRandom().sample(range(capacity), count)
    numbers = []
    for rank in ranks:
        left, right = lower + rank, lower + rank + len(blocked)
        while left < right:
            middle = (left + right) // 2
            available = middle - lower + 1 - bisect_right(blocked, middle)
            if available < rank + 1:
                left = middle + 1
            else:
                right = middle
        numbers.append(left)
    return numbers


def collect_values(input_dir: Path, delimiter: str, decimal_mark: str):
    """Collect shared domains without holding every item row in memory."""
    domains = {name: set() for name in set(ID_DOMAINS.values())}
    amounts = set()
    headers = {}
    counts = {}
    fingerprints = {}
    for filename in SCHEMAS:
        count = 0
        digest = sha256()
        for row in read_rows(input_dir / filename, delimiter, digest):
            count += 1
            for column, domain in ID_DOMAINS.items():
                value = row.get(column, "")
                if value:
                    domains[domain].add(value)
            if filename == ORDERS:
                amount = amount_value(row["TOTALNETAMOUNT"], decimal_mark)
                if amount is not None:
                    amounts.add(amount)
                # Header amounts are repeated across items, never summed.
                header = tuple(
                    amount if column == "TOTALNETAMOUNT" else row[column]
                    for column in SCHEMAS[ORDERS][:-1]
                )
                order = row["SALESORDER"]
                if order:
                    if order in headers and headers[order] != header:
                        raise ValueError("Order rows contain conflicting header values.")
                    headers[order] = header
        counts[filename] = count
        fingerprints[filename] = digest.digest()
    return domains, amounts, counts, fingerprints


def build_mappings(domains, amounts, min_cents: int, max_cents: int):
    id_mappings = {}
    for domain, values in domains.items():
        prefix = ID_PREFIXES[domain]
        numeric_values = values | {value.removeprefix(prefix) for value in values}
        originals = {
            int(value.lstrip("0") or "0") for value in numeric_values
            if value.isascii() and value.isdecimal() and len(value.lstrip("0")) <= 12
        }
        replacements = choose_numbers(len(values), 100_000_000_000, 999_999_999_999, originals)
        id_mappings[domain] = dict(zip(
            sorted(values), (f"{prefix}{number}" for number in replacements),
        ))

    # Exclude original cent-exact magnitudes, even across signs/currencies.
    excluded = set()
    lower = Decimal(f"{min_cents // 100}.{min_cents % 100:02d}")
    upper = Decimal(f"{max_cents // 100}.{max_cents % 100:02d}")
    for value in amounts:
        magnitude = value.copy_abs()
        if lower <= magnitude <= upper:
            numerator, denominator = magnitude.as_integer_ratio()
            cents, remainder = divmod(numerator * 100, denominator)
            if remainder == 0:
                excluded.add(cents)
    amount_mapping = {Decimal(0): "0.00"}
    for sign in (1, -1):
        values = sorted(value for value in amounts if (value > 0 if sign > 0 else value < 0))
        replacements = choose_numbers(len(values), min_cents, max_cents, excluded)
        for original, cents in zip(values, replacements):
            prefix = "-" if sign < 0 else ""
            amount_mapping[original] = f"{prefix}{cents // 100}.{cents % 100:02d}"
    return id_mappings, amount_mapping


def transform(input_dir: Path, output_dir: Path, delimiter: str,
              decimal_mark: str, min_cents: int, max_cents: int) -> dict[str, int]:
    """Validate, transform and publish four files without changing the sources."""
    input_dir = input_dir.resolve()
    output_dir = output_dir.resolve()
    if input_dir.is_relative_to(output_dir) or output_dir.is_relative_to(input_dir):
        raise ValueError("Input and output directories must not overlap.")
    if not input_dir.is_dir():
        raise ValueError("Input directory does not exist.")
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise ValueError("Output directory must be absent or empty; existing files are never overwritten.")
    for filename in SCHEMAS:
        path = input_dir / filename
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing regular input file: {filename}.")

    domains, amounts, counts, fingerprints = collect_values(input_dir, delimiter, decimal_mark)
    id_mappings, amount_mapping = build_mappings(domains, amounts, min_cents, max_cents)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".example-dataset-", dir=output_dir.parent) as temporary:
        build_dir = Path(temporary) / "dataset"
        build_dir.mkdir()
        for filename, columns in SCHEMAS.items():
            written = 0
            digest = sha256()
            with (build_dir / filename).open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=columns, delimiter=";")
                writer.writeheader()
                for row in read_rows(input_dir / filename, delimiter, digest):
                    for column, domain in ID_DOMAINS.items():
                        if row.get(column):
                            try:
                                row[column] = id_mappings[domain][row[column]]
                            except KeyError:
                                raise ValueError("Input changed during processing; retry with stable files.") from None
                    if filename == ORDERS and row["TOTALNETAMOUNT"] != "":
                        amount = amount_value(row["TOTALNETAMOUNT"], decimal_mark)
                        try:
                            row["TOTALNETAMOUNT"] = amount_mapping[amount]
                        except KeyError:
                            raise ValueError("Input changed during processing; retry with stable files.") from None
                    writer.writerow(row)
                    written += 1
            if written != counts[filename] or digest.digest() != fingerprints[filename]:
                raise ValueError("Input changed during processing; retry with stable files.")
        # A directory replacement publishes the completed set, never individual files.
        build_dir.replace(output_dir)
    return counts


def cents_argument(value: str) -> int:
    try:
        amount = Decimal(value)
        if not amount.is_finite() or not Decimal("0.01") <= amount <= Decimal("1000000000000"):
            raise ValueError
        numerator, denominator = amount.as_integer_ratio()
        cents, remainder = divmod(numerator * 100, denominator)
        if remainder:
            raise ValueError
        return cents
    except (InvalidOperation, ValueError, OverflowError):
        raise argparse.ArgumentTypeError(
            "Use an amount from 0.01 to 1000000000000 with at most two decimal places."
        ) from None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-dir", required=True, type=Path, help="Directory containing all four input CSV files, already prepared for conversion.")
    parser.add_argument("--output-dir", required=True, type=Path, help="New or empty directory for the four transformed CSV files.")
    parser.add_argument("--delimiter", choices=(";", ",", "\t"), default=";", help="Input CSV separator (default: semicolon). Output always uses semicolons.")
    parser.add_argument("--decimal-mark", choices=(".", ","), default=".", help="Input monetary decimal mark (default: period); no thousands separators.")
    parser.add_argument("--min-amount", type=cents_argument, default=100, metavar="AMOUNT", help="Minimum replacement magnitude (default: 1.00).")
    parser.add_argument("--max-amount", type=cents_argument, default=10_000_000, metavar="AMOUNT", help="Maximum replacement magnitude (default: 100000.00).")
    args = parser.parse_args()
    if args.min_amount > args.max_amount:
        parser.error("--min-amount must not exceed --max-amount.")
    try:
        counts = transform(args.input_dir, args.output_dir, args.delimiter,
                           args.decimal_mark, args.min_amount, args.max_amount)
    except UnicodeError:
        parser.exit(status=1, message="Error: Input files must contain valid UTF-8 text.\n")
    except csv.Error:
        parser.exit(status=1, message="Error: Invalid CSV structure in an input file.\n")
    except OSError:
        parser.exit(status=1, message="Error: Could not read inputs or publish outputs; check paths, permissions and output contents.\n")
    except (ValueError, InvalidOperation) as exc:
        parser.exit(status=1, message=f"Error: {exc}\n")
    for filename, count in counts.items():
        print(f"Created {filename}: {count} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
