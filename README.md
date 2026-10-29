<div align="center">

# ERP-Customer-Behavior-Analysis

[![Python](https://img.shields.io/badge/Python-3.12-%231D9FD7?style=flat&logo=python&logoColor=%231D9FD7&labelColor=%2330363D)](pyproject.toml)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-%23F37626?style=flat&logo=jupyter&logoColor=%23F37626&labelColor=%2330363D)](src/notebooks)
[![uv](https://img.shields.io/badge/uv-Environment%20Manager-%23DE5FE9?style=flat&logo=uv&logoColor=%23DE5FE9&labelColor=%2330363D)](uv.lock)
[![AI Disclosure](https://img.shields.io/badge/AI-Vibe%20Coding-%236E7681?style=flat&labelColor=%2330363D)](AI_TOOL_DISCLOSURE.md)

Detection, typology and explainable description of purchasing changes in B2B wholesale customers using ERP time series data.

**Open documentation website:** [https://niklasskulll.github.io/ERP-Customer-Behavior-Analysis/docsite/](https://niklasskulll.github.io/ERP-Customer-Behavior-Analysis/docsite/)

</div>

## Table of Contents

- [Overview](#overview)
- [Project status](#project-status)
- [Methodology](#methodology)
- [Getting started](#getting-started)
- [Documentation](#documentation)
- [Project structure](#project-structure)
- [Data conventions](#data-conventions)
- [Data handling](#data-handling)
- [AI assistance](#ai-assistance)
- [License](#license)

---

## Overview

This bachelor's thesis project investigates how changes in customer purchasing behaviour can be detected, classified into interpretable types, and explained using enterprise resource planning (ERP) order data from a B2B wholesaler.

Customer-level time series will describe purchasing dimensions such as revenue, order frequency, basket value, assortment breadth, product-group mix, discounts, and contribution margin. The intended result is a traceable description of **what changed, when it changed, and which purchasing dimensions support the assigned change type**.

The focus is retrospective analysis of purchases observed with the wholesaler. Predicting churn, inferring customers' motives, and deploying a real-time monitoring system are outside the current scope.

Start with the [FUUCKAE framework](docs/framework/fuuckae_framework.md) for the methodology or the [project plan](docs/project/complete_project_plan.md) for the research questions, scope, and proposed thesis structure. The framework is written in English and the project plan is in German.

---

## Project status

**Early research and setup stage.** The repository contains the seven-phase framework, project planning, literature notes, prompt records, and utility scripts. The public notebook directories currently contain placeholders; an end-to-end analysis pipeline and evaluation results are not yet included.

Python dependencies and Jupyter tools are declared in [pyproject.toml](pyproject.toml) and resolved in [uv.lock](uv.lock). The [contributor setup script](setup/initial_setup.sh) prepares the local environment, Git hooks, and Git LFS. Separate example and production configurations are available in [src/config](src/config).

---

## Methodology

**The [FUUCKAE framework](docs/framework/fuuckae_framework.md) organises the work into seven iterative phases:**

| **Phase**                  | **Purpose**                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **1. Frame**               | Define the analysis context and inspect the ERP datasets.                                  |
| **2. Understand**          | Explore customer histories, purchasing patterns, and data usability.                       |
| **3. Unify**               | Prepare the data and construct reliable customer time series.                              |
| **4. Compare**             | Identify candidate changes and describe their timing, magnitude, and persistence.          |
| **5. Knowledge synthesis** | Develop the purchasing-change taxonomy and proposed assignment criteria.                   |
| **6. Apply**               | Assign change types and explain outcomes using recorded evidence and rules.                |
| **7. Evaluate**            | Assess detection, taxonomy applicability, assignment consistency, and explanation quality. |

Candidate detection, taxonomy development, and type assignment are distinct steps. Development evidence and evidence reserved for evaluation are kept separate according to the research claim.

## Getting started

Read the [framework](docs/framework/fuuckae_framework.md) and [data description](docs/project/data_description.md) for the workflow and expected input tables. Documentation can be read without installing Python dependencies.

**After cloning, run the setup script from the repository root:**
```bash
bash setup/initial_setup.sh
```

The script supports Linux, with automatic system-package installation on Ubuntu/Debian, including WSL. Git and an existing clone are required; Python and uv can be installed during setup. Native Windows and macOS setup are not automated by this script.

**Recommended setup:**
- Detects installed tools and offers to install missing Git LFS, uv, and Python.
- Makes the existing Git hooks executable and activates them locally with `git config --local core.hooksPath .githooks`.
- Configures Git LFS locally and downloads files for the checked-out revision, subject to existing LFS download filters.
- Creates or synchronizes `.venv` from the lockfile, including Jupyter and development tools.

The project selects **Python 3.12** through [.python-version](.python-version) and requires **uv 0.13.1 or newer** through `pyproject.toml`. Setup uses `uv sync --locked`; it does not update dependency versions. It can be rerun after an interrupted setup.

**Optional setup commands:**
```bash
bash setup/initial_setup.sh --check     # Inspect setup without changing it
bash setup/initial_setup.sh --yes       # Approve recommended setup and missing-tool installations
bash setup/initial_setup.sh --no-color # Disable colored messages
```

`--check` returns exit code `1` if setup is incomplete. `--yes` stops if conflicting custom Git hooks need approval. See `bash setup/initial_setup.sh --help` for details.

**Start Jupyter from the repository root:**
```bash
PYTHONPATH="$PWD/src" uv run --locked jupyter lab
```

This makes `src/config` importable as `config` from either notebook directory. Select the project interpreter at `.venv/bin/python`. For notebooks run through an editor instead, use the same interpreter and ensure the kernel's `PYTHONPATH` includes the repository's absolute `src` path.

After pulling dependency changes, run `uv sync --locked` again. See the [environment guide](docs/setup/manage_uv_environment.md) for dependency management and activation. Example and production notebook usage is described under [Data handling](#data-handling).

**Utility help commands** use only the Python standard library and do not process data or generate files. Run them from the repository root:

```bash
.venv/bin/python setup/csv_to_parquet.py --help
.venv/bin/python setup/notebook_to_raw_python.py --help
.venv/bin/python setup/create_documentation_site.py --help
```

| **Utility**                                              | **Purpose**                                                                                                                                 | **Execution dependency** |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [CSV to Parquet](setup/csv_to_parquet.py)                | Convert CSV files directly inside `data/data-example/` to compressed Parquet files.                                                         | `duckdb`                 |
| [Notebook export](setup/notebook_to_raw_python.py)       | Export saved source notebooks as Python mirrors without executing cells. See the [conversion guide](docs/setup/create_raw_python_files.md). | `nbconvert`              |
| [Documentation site](setup/create_documentation_site.py) | Generate a local HTML documentation site at `docs/docsite/index.html`.                                                                      | `markdown`               |

The CSV converter currently scans only the selected directory's immediate CSV files. The [data description](docs/project/data_description.md) uses paths under `data/data-example/raw/`. Those paths need to be aligned before using the converter with that layout.

## Documentation

| **Resource**                                                                                 | **Contents**                                                                            |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [FUUCKAE framework](docs/framework/fuuckae_framework.md)                                     | Phase procedures, inputs, outputs, completion criteria, and methodological foundations. |
| [Project plan](docs/project/complete_project_plan.md)                                        | Thesis topic, research questions, metrics, scope, and evaluation proposals.             |
| [Data description](docs/project/data_description.md)                                         | Expected order, product, price, customer, and industry-mapping tables.                  |
| [Literature overview](docs/literature/literature_overview.md)                                | Paper summaries and their relevance to the research question.                           |
| [Bibliography](docs/literature/bibliography.md) · [BibTeX](docs/literature/bibliography.bib) | References used throughout the project.                                                 |
| [Environment setup](docs/setup/manage_uv_environment.md)                                     | Dependency management and environment activation with uv.                               |
| [Contributor setup script](setup/initial_setup.sh)                                          | Interactive installation, local Git hooks, LFS retrieval, and environment setup.        |
| [Notebook configurations](src/config)                                                       | Explicit example and production data and output paths.                                 |
| [Notebook mirror workflow](docs/setup/create_raw_python_files.md)                            | Exporting notebooks for read-only code navigation.                                      |
| [Git LFS setup](docs/setup/git_lfs_setup_handling.md)                                        | Tracking and handling large files.                                                      |
| [MCP Serena setup](docs/setup/mcp_serena_setup.md)                                           | Optional AI-assisted project navigation and client configuration.                       |
| [Prompt records](docs/prompts)                                                               | Prompts used for literature research, framework development, and setup.                 |

## Project structure

**The main documentation and source locations are:**
```text
ERP-Customer-Behavior-Analysis/
├── docs/
│   ├── framework/          # FUUCKAE methodology
│   ├── literature/         # Papers, summaries, and references
│   ├── project/            # Thesis plan and data description
│   ├── prompts/            # Research and development prompt records
│   └── setup/              # Tooling and workflow guides
├── setup/                  # Contributor setup, conversion, and documentation utilities
│   └── initial_setup.sh    # Interactive setup after cloning
├── src/
│   ├── config/             # Shared type and explicit example/production configurations
│   ├── notebooks/          # Authoritative source notebooks
│   ├── .notebooks/         # Private production notebook copies (ignored)
│   └── raw-notebooks/      # Generated Python mirrors for read-only navigation
├── data/
│   ├── data-example/       # Synthetic example inputs and intermediate datasets
│   └── data-prd/           # Private production inputs and intermediate datasets (ignored)
├── outputs/
│   ├── exports/            # Example figures, tables, and other artifacts
│   └── .exports/           # Private production artifacts (ignored)
├── .githooks/              # Production-file guard and Git LFS hooks
├── .python-version        # Project Python version selection
├── pyproject.toml          # Dependencies and minimum uv version
├── uv.lock                 # Resolved dependency versions
├── AI_TOOL_DISCLOSURE.md   # AI tool disclosure
└── README.md
```

## Data conventions

Use these conventions for prepared tables and public examples. Original ERP field names are documented in the [data description](docs/project/data_description.md).

| **Property**          | **Convention**                               | **Example**                              |
| --------------------- | -------------------------------------------- | ---------------------------------------- |
| **Column separator**  | Comma                                        | `,`                                      |
| **Decimal separator** | Period, without thousands separators         | `1234.56`                                |
| **Encoding**          | UTF-8                                        | Supports accented characters and umlauts |
| **Column names**      | English, `snake_case`                        | `monthly_revenue`                        |
| **Date format**       | `YYYY-MM-DD`                                 | `2026-10-21`                             |
| **Table structure**   | One header row, then one observation per row | No extra title or total rows             |

## Data handling

Public examples must use fully synthetic data. The two configurations in `src/config` expose the same properties, so notebook analysis code can use a single `CONFIG` object:

| **Configuration** | **Import** | **`CONFIG.data_dir`** | **`CONFIG.output_dir`** | **`CONFIG.is_production`** |
| ----------------- | ---------- | --------------------- | ---------------------- | -------------------------- |
| Example | `from config.example import CONFIG` | `data/data-example/` | `outputs/exports/` | `False` |
| Production | `from config.production import CONFIG` | `data/data-prd/` | `outputs/.exports/` | `True` |

Paths resolve from the repository root, independently of the notebook's working directory. Configuration imports do not read data or create directories. Neither configuration selects a profile through environment variables or machine detection.

**Workflow across development and production PCs:**
1. Develop the source notebook in `src/notebooks/` with `from config.example import CONFIG` and fully synthetic inputs.
2. Pull the source notebook on the production PC and copy it into the ignored `src/.notebooks/` directory.
3. Change only the private copy's import to `from config.production import CONFIG`. Use a separate kernel for production work.
4. Read datasets through `CONFIG.data_dir` and save intermediate datasets there or generated artifacts under `CONFIG.output_dir`. Create any required output subdirectories explicitly.

**For example, the same analysis code can use either configuration:**
```python
orders = pd.read_parquet(CONFIG.data_dir / "raw/orders.parquet")
tables_dir = CONFIG.output_dir / "tables"
tables_dir.mkdir(parents=True, exist_ok=True)
summary.to_parquet(tables_dir / "summary.parquet", index=False)
```

This snippet assumes `pandas` is imported as `pd` and `summary` has been computed. Both configurations are version-controlled and contain generic paths; production data and results stay in the ignored directories. The repository does not use an `.env` file for this switch.

**Private production notebooks, datasets, and derived exports are excluded through [.gitignore](.gitignore):**
- `src/.notebooks/`
- `data/data-prd/`
- `outputs/.exports/`

The [pre-commit hook](.githooks/pre-commit) checks Git's index for these paths and blocks a commit if any are tracked. The contributor setup script activates this guard and the existing LFS hooks locally. The guard checks paths; it does not detect production results embedded in a public notebook. Keep production imports, saved outputs, and analysis results in private notebook copies.

Edit source notebooks in `src/notebooks/`. Python files in `src/raw-notebooks/` are generated mirrors for read-only inspection; the [mirror guide](docs/setup/create_raw_python_files.md) documents their generation.

## AI assistance

AI tools have supported literature research, framework development, and tooling. See the [AI tool disclosure](AI_TOOL_DISCLOSURE.md) and [prompt records](docs/prompts) for the documentation available so far. The disclosure is still being completed.

## License

No project license file is currently included.
