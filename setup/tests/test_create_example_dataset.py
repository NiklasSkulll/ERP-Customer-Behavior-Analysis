"""Exercise the CSV transformation using entirely invented records."""

import csv
from decimal import Decimal
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import importlib.util


SCRIPT = Path(__file__).resolve().parents[1] / "create_example_dataset.py"
ORDERS = "001_order_header_pos_data.csv"
CUSTOMERS = "002_customer_master_data.csv"
REASONS = "003_order_sddocumentreason_mapping.csv"
INDUSTRIES = "004_customer_industry_mapping.csv"
ORDER_COLUMNS = (
    "SALESORDER SALESORDERTYPE OVERALLSDPROCESSSTATUS SDDOCUMENTREASON "
    "OVERALLSDDOCUMENTREJECTIONSTS SALESORDERDATE SOLDTOPARTY TOTALNETAMOUNT "
    "TRANSACTIONCURRENCY SALESORDERITEM"
).split()


class DatasetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.output = self.root / "output"
        self.write(ORDERS, ORDER_COLUMNS, [
            ["0001", "OR", "A", "01", "A", "2025-01-01", "001", "120.50", "EUR", "10"],
            ["0001", "OR", "A", "01", "A", "2025-01-01", "001", "120.50", "EUR", "20"],
            ["0002", "OR", "B", "02", "B", "2025-02-01", "001", "120.500", "GBP", "10"],
            ["0003", "OR", "C", "99", "C", "2025-03-01", "999", "-12.50", "EUR", "10"],
            ["0004", "OR", "A", "", "A", "2025-04-01", "002", "0", "EUR", "10"],
            ["0005", "OR", "A", "01", "A", "2025-05-01", "002", "", "EUR", "10"],
        ])
        self.write(CUSTOMERS, ["CUSTOMER", "INDUSTRY"],
                   [["001", "I1"], ["002", "I2"], ["003", ""]])
        self.write(REASONS, ["SDDOCUMENTREASON", "SDDOCUMENTREASON_TEXT"],
                   [["01", "Regulär"], ["02", "Sonderfall"], ["03", "Unused"]])
        self.write(INDUSTRIES, ["INDUSTRY", "INDUSTRY_TEXT"],
                   [["I1", "Trade"], ["I2", "Services"], ["I3", "Unused"]])

    def write(self, name, columns, rows, delimiter=";"):
        with (self.source / name).open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, delimiter=delimiter)
            writer.writerow(columns)
            writer.writerows(rows)

    def read(self, folder, name, delimiter=";"):
        with (folder / name).open(encoding="utf-8-sig", newline="") as stream:
            return list(csv.DictReader(stream, delimiter=delimiter))

    def run_script(self, *extra):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--input-dir", str(self.source),
             "--output-dir", str(self.output), *extra],
            capture_output=True, text=True,
        )

    def test_preserves_rows_relationships_and_source_bytes(self):
        before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        result = self.run_script("--min-amount", "20", "--max-amount", "30")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.output.is_dir(), "Expected the transformed dataset directory")
        self.assertEqual({p.name for p in self.output.iterdir()}, set(before))
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.source.iterdir()})
        orders = self.read(self.output, ORDERS)
        original = self.read(self.source, ORDERS)
        self.assertEqual(len(orders), 6)
        changed = {"SALESORDER", "SDDOCUMENTREASON", "SOLDTOPARTY", "TOTALNETAMOUNT"}
        for old, new in zip(original, orders):
            for field in set(ORDER_COLUMNS) - changed:
                self.assertEqual(old[field], new[field])
        self.assertEqual(orders[0]["SALESORDER"], orders[1]["SALESORDER"])
        self.assertEqual(len({r["SALESORDER"] for r in orders}), 5)
        self.assertTrue({r["SALESORDER"] for r in orders}.isdisjoint(
            {r["SALESORDER"] for r in original}))
        customers = self.read(self.output, CUSTOMERS)
        self.assertEqual(orders[0]["SOLDTOPARTY"], customers[0]["CUSTOMER"])
        self.assertEqual(orders[2]["SOLDTOPARTY"], customers[0]["CUSTOMER"])
        self.assertEqual(orders[4]["SOLDTOPARTY"], customers[1]["CUSTOMER"])
        self.assertNotIn(orders[3]["SOLDTOPARTY"], {r["CUSTOMER"] for r in customers})
        self.assertEqual(customers[2]["INDUSTRY"], "")
        reasons = self.read(self.output, REASONS)
        self.assertEqual(orders[0]["SDDOCUMENTREASON"], reasons[0]["SDDOCUMENTREASON"])
        self.assertEqual(orders[2]["SDDOCUMENTREASON"], reasons[1]["SDDOCUMENTREASON"])
        self.assertEqual(reasons[0]["SDDOCUMENTREASON_TEXT"], "Regulär")
        self.assertEqual(orders[4]["SDDOCUMENTREASON"], "")
        industries = self.read(self.output, INDUSTRIES)
        self.assertEqual(customers[0]["INDUSTRY"], industries[0]["INDUSTRY"])
        self.assertEqual(customers[1]["INDUSTRY"], industries[1]["INDUSTRY"])
        self.assertEqual(industries[2]["INDUSTRY_TEXT"], "Unused")
        for rows, column, prefix in (
            (orders, "SALESORDER", "SO"), (orders, "SOLDTOPARTY", "CU"),
            (customers, "CUSTOMER", "CU"), (orders, "SDDOCUMENTREASON", "R"),
            (reasons, "SDDOCUMENTREASON", "R"), (customers, "INDUSTRY", "I"),
            (industries, "INDUSTRY", "I"),
        ):
            for row in rows:
                if row[column]:
                    self.assertRegex(row[column], rf"^{prefix}[0-9]{{12}}$")
        amounts = [r["TOTALNETAMOUNT"] for r in orders]
        self.assertEqual(amounts[0], amounts[1])
        self.assertEqual(amounts[0], amounts[2])
        self.assertTrue(Decimal("20") <= Decimal(amounts[0]) <= Decimal("30"))
        self.assertTrue(Decimal("-30") <= Decimal(amounts[3]) <= Decimal("-20"))
        self.assertEqual(amounts[4:], ["0.00", ""])
        self.assertNotEqual(Decimal(amounts[0]), Decimal("120.50"))

    def test_refuses_existing_output_without_modifying_it(self):
        self.output.mkdir()
        sentinel = self.output / ORDERS
        sentinel.write_text("keep", encoding="utf-8")
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual(sentinel.read_text(), "keep")
        self.assertEqual(list(self.output.iterdir()), [sentinel])

    def test_rejects_input_output_overlap(self):
        for output in (self.source, self.source / "nested", self.root):
            self.output = output
            self.assertNotEqual(self.run_script().returncode, 0)

    def test_rejects_missing_file_without_partial_output(self):
        (self.source / INDUSTRIES).unlink()
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertFalse(self.output.exists())

    def test_rejects_unknown_columns_without_exposing_values(self):
        self.write(CUSTOMERS, ["CUSTOMER", "INDUSTRY", "PRIVATE_NAME"],
                   [["001", "I1", "SECRET_TEST_VALUE"]])
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("SECRET_TEST_VALUE", result.stdout + result.stderr)
        self.assertFalse(self.output.exists())

    def test_rejects_inconsistent_order_headers(self):
        rows = self.read(self.source, ORDERS)
        rows[1]["TOTALNETAMOUNT"] = "121.50"
        self.write(ORDERS, ORDER_COLUMNS, [[r[c] for c in ORDER_COLUMNS] for r in rows])
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("conflicting header", result.stderr)
        self.assertFalse(self.output.exists())

    def test_rejects_invalid_and_nonfinite_amounts_without_exposing_values(self):
        for invalid in ("PRIVATE_INVALID_AMOUNT", "NaN", "Infinity"):
            with self.subTest(amount=invalid):
                rows = self.read(self.source, ORDERS)
                rows[0]["TOTALNETAMOUNT"] = invalid
                self.write(ORDERS, ORDER_COLUMNS, [[r[c] for c in ORDER_COLUMNS] for r in rows])
                result = self.run_script()
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn(invalid, result.stdout + result.stderr)
                self.assertFalse(self.output.exists())

    def test_preserves_header_only_tables(self):
        for name, fields in (
            (ORDERS, ORDER_COLUMNS), (CUSTOMERS, ["CUSTOMER", "INDUSTRY"]),
            (REASONS, ["SDDOCUMENTREASON", "SDDOCUMENTREASON_TEXT"]),
            (INDUSTRIES, ["INDUSTRY", "INDUSTRY_TEXT"]),
        ):
            self.write(name, fields, [])
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in (ORDERS, CUSTOMERS, REASONS, INDUSTRIES):
            self.assertEqual(self.read(self.output, name), [])

    def test_rejects_malformed_rows(self):
        with (self.source / CUSTOMERS).open("a", encoding="utf-8") as stream:
            stream.write("004;I1;EXTRA_PRIVATE_VALUE\n")
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("EXTRA_PRIVATE_VALUE", result.stderr)
        self.assertFalse(self.output.exists())

    def test_decimal_comma_input(self):
        rows = self.read(self.source, ORDERS)
        for row in rows:
            row["TOTALNETAMOUNT"] = row["TOTALNETAMOUNT"].replace(".", ",")
        self.write(ORDERS, ORDER_COLUMNS, [[r[c] for c in ORDER_COLUMNS] for r in rows])
        result = self.run_script("--decimal-mark", ",")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = self.read(self.output, ORDERS)
        self.assertEqual(rows[0]["TOTALNETAMOUNT"], rows[2]["TOTALNETAMOUNT"])
        self.assertNotIn(",", rows[0]["TOTALNETAMOUNT"])

    def test_rejects_changes_between_validation_and_export(self):
        spec = importlib.util.spec_from_file_location("example_dataset", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        collect = module.collect_values

        def change_after_collection(*args):
            result = collect(*args)
            path = self.source / ORDERS
            path.write_bytes(path.read_bytes().replace(b"2025-01-01", b"2025-01-02"))
            return result

        with patch.object(module, "collect_values", side_effect=change_after_collection):
            with self.assertRaisesRegex(ValueError, "changed"):
                module.transform(self.source, self.output, ";", ".", 100, 10_000_000)
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.root.glob(".example-dataset-*")), [])

    def test_rejects_fractional_cent_and_excessive_range_arguments(self):
        for option, value in (
            ("--min-amount", "1.00000000000000000000000000001"),
            ("--max-amount", "1e100"),
        ):
            result = self.run_script(option, value)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(self.output.exists())

    def test_tiny_finite_amounts_are_mapped_without_context_underflow(self):
        rows = self.read(self.source, ORDERS)
        rows[0]["TOTALNETAMOUNT"] = rows[1]["TOTALNETAMOUNT"] = "1e-1000030"
        self.write(ORDERS, ORDER_COLUMNS, [[r[c] for c in ORDER_COLUMNS] for r in rows])
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        amount = Decimal(self.read(self.output, ORDERS)[0]["TOTALNETAMOUNT"])
        self.assertGreater(amount, 0)

    def test_bad_utf8_diagnostics_do_not_echo_input_bytes(self):
        (self.source / CUSTOMERS).write_bytes(b"CUSTOMER;INDUSTRY\n001;\xff\n")
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("0xff", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse(self.output.exists())

    def test_rejects_input_file_symlinks(self):
        path = self.source / INDUSTRIES
        outside = self.root / "other.csv"
        path.replace(outside)
        path.symlink_to(outside)
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertFalse(self.output.exists())

    def test_supports_comma_input_and_empty_output_directory(self):
        for name in (ORDERS, CUSTOMERS, REASONS, INDUSTRIES):
            rows = self.read(self.source, name)
            self.write(name, list(rows[0]), [list(r.values()) for r in rows], delimiter=",")
        self.output.mkdir()
        result = self.run_script("--delimiter", ",")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.output / ORDERS).is_file())
        self.assertEqual(len(self.read(self.output, ORDERS)), 6)

    def test_amount_capacity_failure_leaves_no_output(self):
        self.write(ORDERS, ORDER_COLUMNS, [
            ["1", "OR", "A", "01", "A", "2025-01-01", "001", "10", "EUR", "10"],
            ["2", "OR", "A", "01", "A", "2025-01-02", "001", "20", "EUR", "10"],
        ])
        result = self.run_script("--min-amount", "1.00", "--max-amount", "1.00")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_replacements_are_unique_and_exclude_original_amounts(self):
        self.write(ORDERS, ORDER_COLUMNS, [
            ["1", "OR", "A", "01", "A", "2025-01-01", "001", "1.00", "EUR", "10"],
            ["2", "OR", "A", "01", "A", "2025-01-02", "001", "1.01", "EUR", "10"],
        ])
        result = self.run_script("--min-amount", "1.00", "--max-amount", "1.03")
        self.assertEqual(result.returncode, 0, result.stderr)
        amounts = {r["TOTALNETAMOUNT"] for r in self.read(self.output, ORDERS)}
        self.assertEqual(amounts, {"1.02", "1.03"})


if __name__ == "__main__":
    unittest.main()
