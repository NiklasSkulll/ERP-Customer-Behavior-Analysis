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

The investigation covers a 24-month observation window and uses sales order header information. The three core measures are order count (`ORDERCOUNT`), total net order value (`TOTALORDERNETVALUE`), and average net order value (`AVGORDERNETVALUE`). Customer industry provides context for grouped summaries. Product, assortment, quantity, price-condition, and discount analyses are outside the selected scope. Recorded net order values are not automatically interpreted as realised revenue.

The analytical basis comprises an enriched table with one row per order and monthly profiles keyed by `CUSTOMER_ID`, `PERIODSTART`, and `TRANSACTIONCURRENCY`. Monetary comparisons keep EUR and GBP separate. Monthly profiles can support comparison windows spanning several months; the three stored measures are mathematically related and do not provide independent confirmation of a change.

The intended result is a traceable description of **what changed, when it changed, and which observations support the assigned change type**. The focus is retrospective analysis of purchases observed with the wholesaler. Churn prediction, causal explanations, profitability analysis, production integration, and real-time monitoring are outside the core investigation.

Start with the [bachelor's thesis project plan](docs/project/bachelor_thesis_project_plan.md), the source of truth for research objectives, scope, core measures, and evaluation strategy. The [FUUCCE framework](docs/framework/fuucce_framework.md) operationalises that plan, and the [data description](docs/project/data_description.md) defines the raw, interim, and processed schemas, mappings, and interpretation rules. The [notebook template](docs/project/notebook_template.md) provides the shared structure for the six phase notebooks. These documents are written in English, with German thesis-title and research-question translations in the plan.

---

## Project status

**Research planning and data specifications are established; analytical implementation requires alignment with the current scope.** The repository contains the project plan, six-phase FUUCCE framework, raw and target dataset specifications, notebook and report templates, literature notes, prompt records, and utility scripts. The existing [Phase 1 notebook](src/notebooks/001_f_phase_1.ipynb) contains implementation code but still uses the earlier product/price input schema and measure names. It needs revision against the current header-based scope and notebook template. Later phase notebooks, an end-to-end analysis pipeline, and evaluation results are not yet included. Documented methods describe planned work, not validated findings.

Python dependencies and Jupyter tools are declared in [pyproject.toml](pyproject.toml) and resolved in [uv.lock](uv.lock). The [contributor setup script](setup/initial_setup.sh) prepares the local environment, Git hooks, and Git LFS. Separate example and production configurations are available in [src/config](src/config).

---

## Methodology

**The [FUUCCE framework](docs/framework/fuucce_framework.md) implements the project plan through six phases:**

| **Phase** | **Purpose** |
| --------- | ----------- |
| **1. Familiarise and assess** | Examine source structure, observation coverage, order eligibility, customer histories, and feasibility of the three core measures; establish development and evaluation boundaries. |
| **2. Use data and prepare profiles** | Construct the enriched order-level table and monthly customer-currency profiles, keeping technical validity, analytical eligibility, and measure assessability distinct. |
| **3. Uncover and characterise changes** | Compare reference and subsequent periods and retain change candidates with their supporting evidence. |
| **4. Construct the taxonomy** | Develop distinguishable change types and document their assignment criteria using development cases. |
| **5. Classify and explain** | Apply the criteria automatically and generate evidence-based descriptions, including ambiguity and insufficient evidence. |
| **6. Evaluate and discuss** | Assess detection, taxonomy applicability, assignment quality, and description correctness and completeness. |

Time-window-based comparison of monthly customer profiles is the planned main detection approach. A qualifying change must exceed usual variability, reach a justified minimum magnitude, and have sufficient supporting evidence; this operational definition does not itself imply statistical significance. Exploration proceeds from the data inventory and overall monthly summaries to industry summaries, customer histories, and individual events. An aggregate change is not a prerequisite for examining a customer.

Taxonomy development is researcher-led and data-informed. Documented rules classify change events, allowing compatible labels and explicit ambiguous or unassigned outcomes. Standardised descriptions explain the observed differences and assignment evidence. One notebook per phase follows the [shared template](docs/project/notebook_template.md), recording purpose, inputs, configuration, execution, validation, findings, exports and report, and completion and handoff.

Development is iterative, while final evaluation uses controlled cases and held-out real customer histories. Preparation rules, detection settings, taxonomy criteria, and description rules are fixed before final evaluation; selected sensitivity analyses are reported separately. Description evaluation addresses factual correctness, completeness, and traceability. Without a user study, it does not establish comprehensibility or usefulness for sales staff. Optional refinements, such as ordering-gap descriptions, a second detection method, or expert feedback, follow completion of the core workflow and evaluation.

## Getting started

Read the [project plan](docs/project/bachelor_thesis_project_plan.md) first, followed by the [framework](docs/framework/fuucce_framework.md) and [data description](docs/project/data_description.md) for the workflow and dataset contracts. Use the [notebook template](docs/project/notebook_template.md) when creating or aligning phase notebooks. Documentation can be read without installing Python dependencies.

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

This makes `src/config` importable as `config` from either notebook directory. Select the project interpreter at `.venv/bin/python`. For notebooks run through an editor instead, use the same interpreter and the configuration setup cell in the [notebook template](docs/project/notebook_template.md#notebook-structure), which locates `src` from the working directory and its ancestors. Alternatively, ensure the kernel's `PYTHONPATH` includes the repository's absolute `src` path.

After pulling dependency changes, run `uv sync --locked` again. See the [environment guide](docs/setup/manage_uv_environment.md) for dependency management and activation. Example and production notebook usage is described under [Data handling](#data-handling).

**Utility help commands** use only the Python standard library and do not process data or generate files. Run them from the repository root:

```bash
.venv/bin/python setup/csv_to_parquet.py --help
.venv/bin/python setup/notebook_to_raw_python.py --help
.venv/bin/python setup/create_documentation_site.py --help
```

| **Utility**                                              | **Purpose**                                                                                                                                 | **Execution dependency** |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [CSV to Parquet](setup/csv_to_parquet.py) | Convert immediate CSV files in a selected `raw`, `interim`, or `processed` folder to compressed Parquet files. | `duckdb` |
| [Notebook export](setup/notebook_to_raw_python.py)       | Export saved source notebooks as Python mirrors without executing cells. See the [conversion guide](docs/setup/create_raw_python_files.md). | `nbconvert`              |
| [Documentation site](setup/create_documentation_site.py) | Generate a local HTML documentation site at `docs/docsite/index.html`.                                                                      | `markdown`               |

The CSV converter requires `--folder raw`, `--folder interim`, or `--folder processed`. It reads that folder under `data/data-example/` by default; `--prd` selects the same folder under `data/data-prd/`. It scans only immediate CSV files and writes ZSTD-compressed Parquet files beside them, retaining the CSV originals. Existing Parquet files are skipped unless `--update` is supplied. A missing or empty folder produces an error.

```bash
uv run --locked python setup/csv_to_parquet.py --folder raw
uv run --locked python setup/csv_to_parquet.py --folder interim --update
```

For user-run production conversion, add `--prd` to the corresponding command. Folder selection is required for both environments; commands without `--folder` no longer convert files directly in the data root.

## Documentation

| **Resource**                                                                                 | **Contents**                                                                            |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [Project plan](docs/project/bachelor_thesis_project_plan.md) | Source of truth for objectives, research questions, header-based scope, eligibility principles, core measures, and evaluation strategy. |
| [FUUCCE framework](docs/framework/fuucce_framework.md) | Six-phase workflow with procedures, inputs, outputs, and completion criteria. |
| [Data description](docs/project/data_description.md) | Two main raw ERP datasets, two lookup datasets, their relationships, and the order-level interim and monthly customer-currency target schemas. |
| [Notebook template](docs/project/notebook_template.md) | Shared eight-section structure and configuration setup for one notebook per FUUCCE phase. |
| [Report template](docs/project/report_template.md) | Structure for phase reports presenting findings, run information, validation, and supporting artifacts. |
| [Literature overview](docs/literature/literature_overview.md)                                | Paper summaries and their relevance to the research question.                           |
| [Bibliography](docs/literature/bibliography.md) · [BibTeX](docs/literature/bibliography.bib) | References used throughout the project.                                                 |
| [Environment setup](docs/setup/manage_uv_environment.md)                                     | Dependency management and environment activation with uv.                               |
| [Contributor setup script](setup/initial_setup.sh)                                          | Interactive installation, local Git hooks, LFS retrieval, and environment setup.        |
| [Notebook configurations](src/config)                                                       | Explicit example and production data and output paths.                                 |
| [Notebook mirror workflow](docs/setup/create_raw_python_files.md)                            | Exporting notebooks for read-only code navigation.                                      |
| [Git LFS setup](docs/setup/git_lfs_setup_handling.md)                                        | Tracking and handling large files.                                                      |
| [MCP Serena setup](docs/setup/mcp_serena_setup.md)                                           | Optional AI-assisted project navigation and client configuration.                       |
| [Prompt records](docs/prompts)                                                               | Available literature-research prompt records.                                          |

## Project structure

**The main documentation and source locations are:**
```text
ERP-Customer-Behavior-Analysis/
├── docs/
│   ├── .bachelor-thesis/             # Bachelor thesis LaTeX sources (ignored)
│   ├── docsite/                      # Generated HTML documentation
│   ├── framework/                    # Six-phase FUUCCE methodology
│   │   └── fuucce_framework.md
│   ├── literature/                   # Literature summaries and references
│   │   └── .literature-source-files/ # Scientific papers and source files (ignored)
│   ├── project/                      # Thesis plan, schemas, and phase templates
│   │   ├── bachelor_thesis_project_plan.md # Source of truth for the investigation
│   │   ├── data_description.md        # Raw, interim, and processed dataset contracts
│   │   ├── notebook_template.md       # Shared phase notebook structure and configuration
│   │   └── report_template.md         # Shared phase report structure
│   ├── prompts/                      # Research and development prompt records
│   └── setup/                        # Tooling and workflow guides
├── setup/                            # Contributor setup, conversion, and documentation utilities
│   └── initial_setup.sh              # Interactive setup after cloning
├── src/
│   ├── config/                       # Shared type and explicit example/production configurations
│   ├── notebooks/                    # Authoritative source notebooks
│   ├── .notebooks/                   # Private production notebook copies (ignored)
│   └── raw-notebooks/                # Generated Python mirrors for read-only navigation
├── data/
│   ├── data-example/                 # Synthetic example inputs and intermediate datasets
│   │   ├── raw/                      # Example extracts matching the data description
│   │   ├── interim/                  # Intermediate preparation datasets
│   │   └── processed/                # Prepared analytical datasets
│   └── data-prd/                     # Private production inputs and intermediate datasets (ignored)
├── outputs/
│   ├── exports/                      # Example figures, tables, and other artifacts
│   └── .exports/                     # Private production artifacts (ignored)
├── .githooks/                        # Production-file guard and Git LFS hooks
├── .github/                          # Pull request template
├── .python-version                   # Project Python version selection
├── pyproject.toml                    # Dependencies and minimum uv version
├── uv.lock                           # Resolved dependency versions
├── AI_TOOL_DISCLOSURE.md             # AI tool disclosure
└── README.md
```

## Data conventions

Use these conventions for prepared tables and public examples. Original ERP field names are documented in the [data description](docs/project/data_description.md).

The [framework's file workflow](docs/framework/fuucce_framework.md#data-formats-and-file-workflow) uses Parquet as the standard tabular input format. Export newly created or updated datasets as CSV, convert them to Parquet, and retain both formats. Verify schema and missing-value preservation, and refresh the Parquet version whenever its CSV changes. The CSV converter's folder selection is described under [Getting started](#getting-started).

| **Property**              | **Convention**                               | **Example**                              |
| ------------------------- | -------------------------------------------- | ---------------------------------------- |
| **CSV column separator**  | Semicolon for prepared outputs               | `;`                                      |
| **Encoding**              | UTF-8                                        | Supports accented characters and umlauts |
| **Column names**          | Uppercase; preserve ERP codes and documented derived names | `CUSTOMER_ID`, `TOTALORDERNETVALUE` |
| **Dates**                 | ISO calendar dates                           | `2026-03-01`                             |
| **Monetary values**       | Decimal point, no thousands separators        | `1234.50`                                |
| **Missing values**        | Empty CSV fields                             | Preserve missingness when reloading      |
| **Identifiers and codes** | Load as strings, preserving leading zeros     | `000123`                                 |

Preserve raw extracts in their original format and verify their actual import settings. For prepared profiles, count distinct eligible orders and retain each order's header amount once. An eligible order with a missing amount still contributes to the count, but its affected total and average remain missing. Broader monetary aggregates also remain missing when a required contributing total is unavailable. Recompute aggregate averages from complete totals and counts.

Record zero count and total only where observation coverage supports zero eligible activity; leave the average missing for zero-order periods. Missing coverage is not inactivity. Keep monetary summaries within a currency and retain customers with missing industry assignments. Detailed eligibility, calculation, and validation rules remain in the project plan and data description.

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
3. Select `from config.production import CONFIG` in the private copy. When using the template's path-discovery cell, also change its configuration-file check to `production.py`. Use a separate kernel for production work.
4. Read datasets through `CONFIG.data_dir` and save intermediate datasets there or generated artifacts under `CONFIG.output_dir`. Create any required output subdirectories explicitly.

**For example, the same analysis code can use either configuration:**
```python
orders = pd.read_parquet(CONFIG.data_dir / "interim/001_order_header_data.parquet")
# Construct monthly_profiles from eligible orders using the documented schema.
processed_dir = CONFIG.data_dir / "processed"
processed_dir.mkdir(parents=True, exist_ok=True)
monthly_profiles.to_csv(
    processed_dir / "001_customer_monthly_profiles.csv", sep=";", index=False
)
```

This snippet assumes `pandas` is imported as `pd`, the interim Parquet input has been prepared, and `monthly_profiles` has been computed. Convert the exported CSV with `--folder processed` (adding `--update` when refreshing an existing Parquet file and `--prd` for user-run production conversion), then verify schema, identifiers, monetary precision, and missingness before reuse. Both configurations are version-controlled and contain generic paths; production data and results stay in the ignored directories. The repository does not use an `.env` file for this switch.

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
