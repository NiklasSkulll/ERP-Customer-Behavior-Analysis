"""Convert project CSV files to Parquet. Requires: uv add duckdb."""

import argparse
from pathlib import Path
import sys

def main() -> int:
    # Create argument parser and arguments like '--help', '--prd' and '--update'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prd", action="store_true",
        help="Read data/data-prd instead of data/data-example.",
    )
    parser.add_argument(
        "--update", action="store_true",
        help="Replace existing Parquet files with newly converted CSV content.",
    )
    args = parser.parse_args()

    # Resolve project root path, relative to this script
    project_root = Path(__file__).resolve().parent.parent

    # Resolve project data paths as 'source_dir'
    source_dir = project_root / "data" / (
        "data-prd" if args.prd else "data-example"
    )
    if not source_dir.is_dir():
        parser.exit(status=1, message=f"Error: Directory does not exist: {source_dir}\n")

    # Find all CSV files and store in 'sources'
    sources = sorted(path for path in source_dir.glob("*.csv") if path.is_file())
    if not sources:
        parser.exit(status=1, message=f"Error: No CSV files found in: {source_dir}\n")

    # Import DuckDB package
    try:
        import duckdb
    except ImportError:
        parser.exit(status=1, message=f"Error: Missing dependency. Install it with: uv add duckdb\n")

    # Initialize the failures count for files that failed conversion
    failures = 0

    # Opens a DuckDB connection and converts CSV to parquet files
    with duckdb.connect() as con:
        for source in sources:
            target = source.with_suffix(".parquet")
            temp_target = target.with_suffix(".tmp.parquet")

            if target.exists() and not args.update:
                print(f"Skipping existing file: {target.name}")
                continue

            try:
                # Write the new data to a temporary file first
                con.read_csv(str(source), header=True).write_parquet(
                    str(temp_target), compression="zstd"
                )

                # Replace the final file only after conversion succeeds
                temp_target.replace(target)
            except (duckdb.Error, OSError) as exc:
                # Clean up the temporary file if it exists
                try:
                    temp_target.unlink(missing_ok=True)
                except OSError as cleanup_exc:
                    print(f"Could not remove temporary file: {cleanup_exc}", file=sys.stderr)

                print(f"Failed: {source.name}: {exc}", file=sys.stderr)
                failures += 1
            else:
                print(f"Converted: {source.name} -> {target.name}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
