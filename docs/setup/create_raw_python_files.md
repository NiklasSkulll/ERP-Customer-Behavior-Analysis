<div align="center">

# Create raw Python files from Jupyter notebooks

This guide explains how to generate Python mirror files using the project's `notebook_to_raw_python.py` script within the uv-managed environment. The script uses `nbconvert` internally.

The notebooks remain authoritative. Generated mirrors support read-only code navigation and inspection through MCP Serena.

> The environment setup uses uv, and the conversion script uses nbconvert to export notebooks as Python files (Astral, n.d.; Jupyter Development Team, n.d.a, n.d.b). The script's command-line interface, mirror naming convention, and read-only workflow are project-specific.

</div>

## Table of Contents

- [Convert Jupyter notebooks to raw Python files](#convert-jupyter-notebooks-to-raw-python-files)
    - [Before converting](#before-converting)
    - [Convert one notebook](#convert-one-notebook)
    - [Convert all notebooks](#convert-all-notebooks)
    - [View command-line help](#view-command-line-help)
    - [Maintain the generated mirrors](#maintain-the-generated-mirrors)
- [Conversion results and errors](#conversion-results-and-errors)
- [Bibliography](#bibliography)

---

## Convert Jupyter notebooks to raw Python files

Run the examples below from the repository root using `setup/notebook_to_raw_python.py`. The script determines the repository root from its own location, then reads notebooks from `src/notebooks` and writes mirrors to `src/raw-notebooks`. Each mirror retains the notebook's base name with an added `_mirror` suffix and a `.py` extension.

**Subdirectory structure is preserved:**

| **Source notebook**                     | **Generated mirror**                            |
| --------------------------------------- | ----------------------------------------------- |
| `src/notebooks/01_Phase.ipynb`          | `src/raw-notebooks/01_Phase_mirror.py`          |
| `src/notebooks/analysis/02_Model.ipynb` | `src/raw-notebooks/analysis/02_Model_mirror.py` |

Output directories are created automatically when needed.

### Before converting

> **Before the first conversion:** Follow the [environment guide](manage_uv_environment.md) to prepare the project environment and ensure `nbconvert` is installed. Run all conversion commands below from the repository root.

Save the notebooks first. Conversion reads the saved files on disk. It does not save open notebooks, execute cells, or modify source notebooks.

**Mirrors are generated files:** agents may read them but must not edit or regenerate them. Run conversion yourself after notebook changes and before asking Serena to inspect the updated code.

### Convert one notebook

**Pass a notebook path relative to `src/notebooks`:**
```bash
uv run --locked python setup/notebook_to_raw_python.py --file 01_Phase.ipynb
```

**For a notebook in a subdirectory:**
```bash
uv run --locked python setup/notebook_to_raw_python.py --file analysis/02_Model.ipynb
```

Do not prefix relative `--file` paths with `src/notebooks/`. The script adds that directory itself.

Absolute paths are also accepted, provided they point to an existing `.ipynb` file inside `src/notebooks`. Paths that resolve outside that directory are rejected.

### Convert all notebooks

```bash
uv run --locked python setup/notebook_to_raw_python.py --all-files
```

This recursively finds and converts notebooks beneath `src/notebooks`, excluding `.ipynb_checkpoints` directories. Explicitly selecting a checkpoint notebook with `--file` is also rejected.

Each run requires exactly one conversion mode: `--file` or `--all-files`. They cannot be combined.

### View command-line help

```bash
uv run --locked python setup/notebook_to_raw_python.py --help
```

### Maintain the generated mirrors

Mirror names and output locations are assigned automatically. No output-name or output-directory arguments are needed.

Successful conversion replaces the corresponding mirror. The script writes to a temporary file before replacing the destination, so a failed conversion or write leaves an existing mirror intact.

**The script does not detect unchanged notebooks:** `--all-files` re-exports every selected notebook.

After renaming or deleting a notebook, manually remove its obsolete mirror. The script does not clean up stale mirrors. Markdown cells may appear as comments in the generated Python files.

---

## Conversion results and errors

The script prints a `Converted:` message for each successful export and a `Failed:` message for each notebook that could not be converted.

If one notebook fails during conversion, the script continues processing the remaining selected notebooks. Successful exports remain in place. The batch is not rolled back. After processing, the script reports the number of successful and failed conversions and the output directory.

| **Exit code** | **Meaning**                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `0`           | All selected notebooks were converted successfully or help was displayed.       |
| `1`           | A setup or discovery error occurred or at least one notebook failed to convert. |
| `2`           | Invalid command-line arguments or an invalid explicit notebook selection.       |

Common causes of failure include a missing `src/notebooks` directory, no notebooks found with `--all-files`, a missing `nbconvert` dependency, invalid notebook contents, or output permission problems.

Startup errors stop the script before the conversion summary is printed. If `uv` fails before launching Python, its own error and exit status apply.

---

## Bibliography

See [docs/literature/bibliography.md](../literature/bibliography.md).
