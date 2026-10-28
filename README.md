<div align="center">

# ERP-Customer-Behavior-Analysis

[![Python](https://img.shields.io/badge/Python-3.12-%231D9FD7?style=flat&logo=python&logoColor=%231D9FD7&labelColor=%23082A2E)](pyproject.toml)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-%23F37626?style=flat&logo=jupyter&logoColor=%23F37626&labelColor=%23082A2E)](src/notebooks)
[![uv](https://img.shields.io/badge/uv-Environment%20Manager-%23DE5FE9?style=flat&logo=uv&logoColor=%23DE5FE9&labelColor=%23082A2E)](uv.lock)
[![AI Disclosure](https://img.shields.io/badge/AI-Vibe%20Coding-%237F7F7F?style=flat&labelColor=%23082A2E)](AI_TOOL_DISCLOSURE.md)

Detection, typology and explainable description of purchasing changes in B2B wholesale customers using ERP time series data.

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

`pyproject.toml` and `uv.lock` are currently empty placeholders. A reproducible dependency environment still needs to be configured before the analysis can be run.

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

1. Read the [framework](docs/framework/fuuckae_framework.md) and [data description](docs/project/data_description.md) to understand the workflow and expected input tables. The documentation can be read without installing Python dependencies.
2. For code execution, use Python 3.11 and uv as the intended tooling. Follow the [environment guide](docs/setup/manage_uv_environment.md) once the dependency configuration is populated; `uv sync --locked` is not a working bootstrap command with the current empty configuration files.
3. Review the utility scripts below. Run commands from the project root. Their help commands use only the Python standard library and do not process data or generate files.

```bash
python3 setup/csv_to_parquet.py --help
python3 setup/notebook_to_raw_python.py --help
python3 setup/create_documentation_site.py --help
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
├── setup/                  # Conversion and documentation utilities
├── src/
│   ├── notebooks/          # Authoritative source notebooks
│   └── raw-notebooks/      # Generated Python mirrors for read-only navigation
├── env/
│   └── .env.example        # Local configuration template
├── pyproject.toml          # Project configuration placeholder
├── uv.lock                 # Dependency lockfile placeholder
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

Public examples should use synthetic data.

**Private production notebooks, datasets, and derived exports are excluded through [.gitignore](.gitignore):**
- `src/.notebooks/`
- `data/data-prd/`
- `outputs/.exports/`

The [pre-commit hook](.githooks/pre-commit) checks Git's index for these paths and blocks a commit if any are tracked.

**After initialising a local Git repository, enable the hook with:**
```bash
git config core.hooksPath .githooks
```

Edit source notebooks in `src/notebooks/`. Python files in `src/raw-notebooks/` are generated mirrors for read-only inspection; the [mirror guide](docs/setup/create_raw_python_files.md) documents their generation.

## AI assistance

AI tools have supported literature research, framework development, and tooling. See the [AI tool disclosure](AI_TOOL_DISCLOSURE.md) and [prompt records](docs/prompts) for the documentation available so far. The disclosure is still being completed.

## License

No project license file is currently included.
