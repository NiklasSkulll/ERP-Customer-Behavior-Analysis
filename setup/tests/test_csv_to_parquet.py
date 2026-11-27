"""Run the CSV converter only in temporary trees with invented records."""

import csv
from datetime import date
from decimal import Decimal
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import pyarrow as pa
import pyarrow.parquet as pq


SCRIPT = Path(__file__).resolve().parents[1] / "csv_to_parquet.py"


class CsvToParquetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "setup").mkdir()
        self.script = self.root / "setup/csv_to_parquet.py"
        shutil.copyfile(SCRIPT, self.script)

    def write_fixture(self, stage="raw", profile="data-example", amount="1234.50"):
        folder = self.root / "data" / profile / stage
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "orders.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["CUSTOMER_ID", "SALESORDERDATE", "TOTALNETAMOUNT", "DESCRIPTION"])
            writer.writerows([
                ["CU000000000001", "2025-01-01", amount, "Invented; Süd"],
                ["CU000000000002", "2025-02-01", "-25.75", "Second"],
                ["CU000000000003", "2025-03-01", "", ""],
            ])
        return path

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(self.script), *args],
            cwd=self.root, capture_output=True, text=True,
        )

    def test_round_trip_for_each_stage_and_profile(self):
        # The second profile is also fully invented and lives only in /tmp.
        for profile, extra in (("data-example", []), ("data-prd", ["--prd"])):
            for stage in ("raw", "interim", "processed"):
                with self.subTest(profile=profile, stage=stage):
                    source = self.write_fixture(stage, profile)
                    before = source.read_bytes()
                    result = self.run_script("--folder", stage, *extra)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    table = pq.read_table(source.with_suffix(".parquet"))
                    self.assertEqual(table.column_names, [
                        "CUSTOMER_ID", "SALESORDERDATE", "TOTALNETAMOUNT", "DESCRIPTION",
                    ])
                    self.assertEqual(table.schema.field("CUSTOMER_ID").type, pa.string())
                    self.assertEqual(table.schema.field("SALESORDERDATE").type, pa.date32())
                    rows = table.to_pylist()
                    self.assertEqual([r["CUSTOMER_ID"] for r in rows], [
                        "CU000000000001", "CU000000000002", "CU000000000003",
                    ])
                    self.assertEqual(rows[0]["SALESORDERDATE"], date(2025, 1, 1))
                    self.assertEqual(Decimal(str(rows[0]["TOTALNETAMOUNT"])), Decimal("1234.50"))
                    self.assertEqual(Decimal(str(rows[1]["TOTALNETAMOUNT"])), Decimal("-25.75"))
                    self.assertIsNone(rows[2]["TOTALNETAMOUNT"])
                    self.assertIsNone(rows[2]["DESCRIPTION"])
                    self.assertEqual(rows[0]["DESCRIPTION"], "Invented; Süd")
                    self.assertEqual(source.read_bytes(), before)
                    self.assertFalse(source.with_suffix(".tmp.parquet").exists())
                    self.assertTrue(all(
                        pq.ParquetFile(source.with_suffix(".parquet")).metadata
                        .row_group(0).column(i).compression == "ZSTD"
                        for i in range(table.num_columns)
                    ))

    def test_existing_parquet_is_skipped_until_update_is_requested(self):
        source = self.write_fixture()
        self.assertEqual(self.run_script("--folder", "raw").returncode, 0)
        target = source.with_suffix(".parquet")
        before = target.read_bytes()
        self.write_fixture(amount="4321.25")
        result = self.run_script("--folder", "raw")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(target.read_bytes(), before)
        result = self.run_script("--folder", "raw", "--update")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(pq.read_table(target).to_pylist()[0]["TOTALNETAMOUNT"], 4321.25)
        self.assertNotEqual(target.read_bytes(), before)

    def test_only_immediate_csv_files_in_selected_stage_are_converted(self):
        source = self.write_fixture()
        nested = source.parent / "nested/ignored.csv"
        nested.parent.mkdir()
        nested.write_text("ID;VALUE\nCU1;1\n", encoding="utf-8")
        other = self.write_fixture(stage="processed")
        result = self.run_script("--folder", "raw")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(source.with_suffix(".parquet").is_file())
        self.assertFalse(nested.with_suffix(".parquet").exists())
        self.assertFalse(other.with_suffix(".parquet").exists())

    def test_invalid_missing_and_empty_stage_fail(self):
        for args in ((), ("--folder", "unknown"), ("--folder", "raw")):
            with self.subTest(args=args):
                self.assertNotEqual(self.run_script(*args).returncode, 0)
        (self.root / "data/data-example/raw").mkdir(parents=True)
        self.assertNotEqual(self.run_script("--folder", "raw").returncode, 0)

    def test_failed_update_keeps_previous_parquet_and_cleans_temporary_file(self):
        source = self.write_fixture()
        self.assertEqual(self.run_script("--folder", "raw").returncode, 0)
        target = source.with_suffix(".parquet")
        before = target.read_bytes()
        source.write_bytes(b"ID;VALUE\nCU1;\xff\n")
        result = self.run_script("--folder", "raw", "--update")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.read_bytes(), before)
        self.assertFalse(source.with_suffix(".tmp.parquet").exists())


if __name__ == "__main__":
    unittest.main()
