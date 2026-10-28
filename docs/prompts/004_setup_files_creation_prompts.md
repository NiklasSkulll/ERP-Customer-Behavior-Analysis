<div align="center">

# Prompts used for creating the setup files

[![GPT-6 Astra](https://img.shields.io/badge/GPT--6%20Astra-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-astra)

</div>

## Table of Contents

- [Prompts to create a Python file for converting CSV to Parquet](#prompts-to-create-a-python-file-for-converting-csv-to-parquet)
    - [Initial prompts to create the first setup version](#initial-prompts-to-create-the-first-setup-version)
    - [Prompt used to understand the Python script](#prompt-used-to-understand-the-python-script)
    - [Prompts used for development](#prompts-used-for-development)
- [Prompts to create a Python file for creating the documentation sites](#prompts-to-create-a-python-file-for-creating-the-documenation-sites)
    - [Initial prompts to create the first setup version](#initial-prompts-to-create-the-first-setup-version-1)
    - [Prompts used for development](#prompts-used-for-development-1)
- [Prompts to create a Python file for converting notebooks to raw Python files](#prompts-to-create-a-python-file-for-converting-notebooks-to-raw-python-files)
- [Bibliography](#bibliography)

---

## Prompts to create a Python file for converting CSV to Parquet

> This setup `setup/csv_to_parquet.py` got created all in one chat.

### Initial prompts to create the first setup version

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> An existing chat with a question about csv file format was used to create this setup (see initial prompt below).

**Initial Prompt:**
```markdown
**Topic:** Programming, GitHub, Data analysis

**Background:** I have a programming project and I'm doing the repo and documentation. I want to analyze data using Python notebooks.

**Task:**
- What's the best practice for CSV files? For example, if I convert an Excel worksheet to CSV, I can separate the values with `;` or `,`. What would be best in my case?
```

**Prompt to prepare the script creation:**
```markdown
I'm working with big data in my project and have CSV files. I've heard that Parquet files are better than CSV files. Can I convert them to Parquet without too much effort? Does that make sense?
```

**Prompt to create the script:**
```markdown
Ok thanks. Now I want to create a python script file in `setup/csv_to_parquet.py` to convert all my CSV files to Parquet files.

Can I have something like params in such a script aswell? For this logic: "Standard is to convert all files in `data/data-example/*.csv` but when starting the script with e.g. `--prd` it converts all CSV files in `data/data-prd/*.csv` instead using the example path.

Please create the script.
```

### Prompt used to understand the Python script

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
Explain me every line of this Python script very simple, so that I can edit and understand it.

**Your Script:**

#!/usr/bin/env python3
"""Convert project CSV files to Parquet. Requires: pip install duckdb."""

import argparse
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prd", action="store_true",
        help="Read data/data-prd instead of data/data-example.",
    )
    args = parser.parse_args()

    # Resolve paths relative to this script, independent of the working directory.
    project_root = Path(__file__).resolve().parent.parent
    source_dir = project_root / "data" / (
        "data-prd" if args.prd else "data-example"
    )
    if not source_dir.is_dir():
        parser.error(f"Directory does not exist: {source_dir}")
    sources = sorted(source_dir.glob("*.csv"))
    if not sources:
        parser.error(f"No CSV files found in: {source_dir}")

    try:
        import duckdb
    except ImportError:
        parser.error("Missing dependency. Install it with: python -m pip install duckdb")

    failures = 0
    with duckdb.connect() as con:
        for source in sources:
            target = source.with_suffix(".parquet")
            if target.exists():
                print(f"Skipping existing file: {target.name}")
                continue
            try:
                # DuckDB detects CSV delimiters and column types automatically.
                con.read_csv(str(source), header=True).write_parquet(
                    str(target), compression="zstd"
                )
            except duckdb.Error as exc:
                # Remove an incomplete output so a later run can retry.
                target.unlink(missing_ok=True)
                print(f"Failed: {source.name}: {exc}", file=sys.stderr)
                failures += 1
            else:
                print(f"Converted: {source.name} -> {target.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

```

### Prompts used for development

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is a prompt that got used to improve and develop the Python setup script. After that, the setup got improved and reviewed step-by-step.

**Prompt:**
```markdown
Is this `#!/usr/bin/env python3` good for my workspacce with uv (uv.lock) and pyproject.toml? and with `Python 3.12.3`? What I meant is do I need this line in the script? And why?
[...]
I added a param called `--update`, so files can be updated by choice. How can I edit this part to include it properly and why? Is it simply by changing the if condition to `target.exists() and not args.update`?

**Part, I added:**

target = source.with_suffix(".parquet")

            if target.exists():
                print(f"Skipping existing file: {target.name}")
                continue
```

**Final Prompt:**
```markdown
Is this now good and works without failures?

**My current script:**

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
        help="Update existing parquet files with the CSV file content.",
    )
    args = parser.parse_args()

    # Resolve project root path, relative to this script
    project_root = Path(__file__).resolve().parent.parent

    # Resolve project data paths as 'source_dir'
    source_dir = project_root / "data" / (
        "data-prd" if args.prd else "data-example"
    )
    if not source_dir.is_dir():
        parser.error(f"Directory does not exist: {source_dir}")

    # Find all CSV files and store in 'sources'
    sources = sorted(source_dir.glob("*.csv"))
    if not sources:
        parser.error(f"No CSV files found in: {source_dir}")

    # Import DuckDB package
    try:
        import duckdb
    except ImportError:
        parser.error("Missing dependency. Install it with: uv add duckdb")

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
                # Copy file as target and delete temp or rename temp as target
                print(f"Converted: {source.name} -> {target.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

```

---

## Prompts to create a Python file for creating the documentation sites

> This setup `setup/create_documentation_site.py` got created all in one chat.

### Initial prompts to create the first setup version

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
**I have an Idea:** I have a programming repo for my Bachelor Thesis and I am currently setting it up. I need to do a data analysis with Python in Jupyter notebooks. I want to create a Python script in a file `setup/create_documentation_site.py`.

**The script should do the following:**
- look into `docs` and its subfolders, look for all `md` files.
- then convert the files to `html` files with nice css.
- create a overall `index.html` which links all other `html` files, so that I have a nice documentation overview for my repo.

As context I give you my Bachelor Thesis Plan (but I dont think we need this for my script) and a script I did create for my repo to convert CSV to Parquet. **First only tell me:** Is this possible? Yes/No and is it simple? Yes/No and why?
```

**Follow-up-Prompt:**
```markdown
I want to do this with you then. Following Python best practices. I dont know the imports I need to do. And I think my logic does not look for documentation in subfolders (see below).

**In addition:** What do you think: does `--update` as param is enough? or not? Do I need a param here?

**Would I start the script with this?**

"""Convert project documentation Markdown files to HTML and combine to a documentation site."""

# import packages...

def main() -> int:
    # Create argument parser and arguments like '--help' and '--update'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update", action="store_true",
        help="Update existing HTML files with the Markdown files content.",
    )
    args = parser.parse_args()

    # Resolve project root path, relative to this script
    project_root = Path(__file__).resolve().parent.parent

    # Resolve project data paths as 'source_dir'
    source_dir = project_root / "docs"

    if not source_dir.is_dir():
        parser.error(f"Directory does not exist: {source_dir}")

    # Find all CSV files and store in 'sources'
    sources = sorted(source_dir.glob("*.md"))
    if not sources:
        parser.error(f"No Markdown files found in: {source_dir} and its subfolders.")

    target_dir = project_root / "docs" / "docsite"
```

### Prompts used for development

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is a prompt that got used to improve and develop the Python setup script, after some questions of understanding. After that, the setup got improved and reviewed step-by-step.

**Prompt:**
```markdown
Ok and what now? What is the next step for my script and what should I write and why?
Use current Python best practices.
```

---

## Prompts to create a Python file for converting notebooks to raw Python files

> This setup `setup/notebook_to_raw_python.py` got created all in one chat.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> After the following prompt, comprehension questions were asked.

**Prompt:**
```markdown
**Role:** You are an expert in programming with Python and you know all the best practices in creating Python scripts.

**Task:** I have a Python data analysis repo, I am currently setting up. I thought about creating a setup script, which converts my Python notebooks to raw Python mirror files. I once created a documentation to convert it manually (look at `create_raw_python_files.md`). Analyse my other Python setup files (`create_documentation_site.py`, `csv_to_parquet.py`) as reference for my script structure, etc.

How should such a script look like? Below is the begin of the script I want to create. Look and analyse it and improve it. In addition: create the final setup script, for my case.

**In the same place as the other scripts I created `setup/notebook_to_raw_python.py` in my repo:**

"""Convert project Jupyter notebooks to raw Python files (mirror files)."""

import argparse
from pathlib import Path
import sys

def main() -> int:
    # Create argument parser and arguments like '--help', '--prd' and '--update'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all-files", action="store_true",
        help="Convert all existing Jupyter notebooks to raw Python files.",
    )
    parser.add_argument(
        "--file", action="store_true",
        help="Convert one specific Jupyter notebooks to a raw Python file.",
    )
    args = parser.parse_args()

    # Resolve project root path, relative to this script
    project_root = Path(__file__).resolve().parent.parent

    # Resolve project Python and notebook paths as 'source_dir' and 'target_dir'
    src_root = project_root / "src"
    source_dir = src_root / "notebooks"
    target_dir = src_root / "raw-notebooks"
```

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
