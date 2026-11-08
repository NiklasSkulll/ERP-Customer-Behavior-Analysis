<div align="center">

# Notebook template

A shared structure for the six [FUUCCE phase](docs/framework/fuucce_framework.md) notebooks, supporting consistent documentation, reproducible execution and traceable analytical decisions.

</div>

## Table of Contents

- [Overview](#overview)
- [Notebook structure](#notebook-structure)

---

## Overview

This document defines the common structure for the project's Jupyter notebooks, with one notebook dedicated to each [FUUCCE phase](docs/framework/fuucce_framework.md). Each notebook records its purpose, inputs, configuration, analytical steps, validation results and findings, followed by exports and the handoff to subsequent work.

The template provides a consistent organisational structure without prescribing identical analyses. Phase-specific tasks, required outputs and completion criteria remain defined by the [FUUCCE framework](docs/framework/fuucce_framework.md). Methodological explanations and interpretations belong in Markdown cells, while executable analysis and checks belong in code cells.

---

## Notebook structure

Use the following headings as the starting point for each phase notebook. Replace the placeholders with the phase number and name, and expand the sections with appropriate Markdown and code cells. The bullet points describe the expected content and should be replaced with concrete explanations, procedures and findings.

Keep the main section order consistent and add subsections where needed. If an item does not apply, briefly explain why. Present validation checks and relevant findings alongside the analytical steps where useful. The dedicated sections consolidate their outcomes.

**Notebook structure:**
```markdown
# Phase <No.> - <Phase Name>

## 1 Purpose and context

- Purpose of the phase.
- Relevant research questions.
- Expected results.
- Reference to the framework.

## 2 Inputs and prerequisites

- Required data.
- Results from previous phases.
- Data version, observation period and preparation status.
- Role as evidence for development or evaluation.

## 3 Configuration

- Data profile.
- Paths.
- Relevant parameters.
- If applicable, random seed.

## 4 Execution

- Phase-specific analysis steps with brief methodological justifications.

## 5 Validation of results

- Data and plausibility checks.
- Computational and methodological consistency.
- Failed checks.

## 6 Findings and decisions

- Key results.
- Interpretation.
- Decisions made.
- Limitations.

## 7 Exports and report

- Saved artifacts.
- Report.
- Information about the execution run.

## 8 Completion and handoff

- Completion criteria met.
- Open issues.
- Specific inputs required for the next phase.
```

Place the following code in the configuration section before loading data or writing outputs. It locates the project's source directory and makes the configuration package importable when the kernel's working directory is the repository root or one of its subdirectories.

Use the example configuration in public source notebooks. In a user-managed private production copy, change the configuration import to `from config.production import CONFIG` and the config check to `folder / "src" / "config" / "production.py"`. Use `CONFIG.data_dir` and `CONFIG.output_dir` consistently for subsequent file operations.

**Import of the configuration:**
```python
# CONFIG roots derive from the repository location, not the kernel's working directory.
from pathlib import Path
import sys

# Find src starting from the working directory and its ancestor directories.
cwd = Path.cwd()

# In a user-managed private copy, select "production.py" instead of "example.py".
for folder in (cwd, *cwd.parents):
    if (folder / "src" / "config" / "example.py").is_file():
        src_path = folder / "src"
        break
else:
    raise FileNotFoundError(
        f"src/config/example.py was not found relative to {cwd}."
    )

if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Load configuration. In a user-managed private copy, select config.production instead of config.example.
from config.example import CONFIG
```
