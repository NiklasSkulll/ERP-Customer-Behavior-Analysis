<div align="center">

# Report template

A shared structure for the six [FUUCCE phase](docs/framework/fuucce_framework.md) reports, presenting key findings and linking the supporting figures, tables and datasets. [setup/create_markdown_report.py](setup/create_markdown_report.py) implements this structure to generate phase reports.

</div>

## Table of Contents

- [Overview](#overview)
- [Report structure](#report-structure)

---

## Overview

This document defines the common structure for the Markdown reports accompanying the six [FUUCCE phase](docs/framework/fuucce_framework.md) notebooks. Each report provides a concise account of the phase's results, the data used and the artifacts produced.

The notebook documents the analytical procedure and methodological reasoning. The report presents selected findings and their supporting evidence in a form that can be read without executing or opening the notebook. Include enough context to explain what each result shows and which limitations affect its interpretation.

Reports are generated from explicitly supplied results, descriptions and artifact references. Numerical summaries and file references can be populated automatically; interpretations and decisions require author review.

Save each report under the configured output directory alongside its supporting exports. Reports based on production data must remain in the private production output directory.

---

## Report structure

Use the following structure for each phase report. Replace the placeholders with the phase number and name, and adapt the results subsections to the phase's required outputs.

Embed selected figures using standard Markdown image syntax. Present small tables directly in Markdown and link larger tables or datasets. Use paths relative to the report file for local images and links.

Describe each linked dataset's role and content briefly. Distinguish input datasets from newly created datasets, and identify the data version or snapshot used.

**Report directory and file name:**
- _Directory:_ `outputs/exports/reports` or `outputs/.exports/reports`
- _File name:_ `00<phase no.>_<phase letter>_phase_report.md`

**Report structure:**
```markdown
# Phase <No.> - <Phase Name>: Report

## 1 Purpose and run information

- Purpose and scope of the phase.
- Source notebook.
- Run identifier and execution date.
- Data profile: example or production.
- Development or evaluation context.
- Relevant code, data and specification versions.
- Key parameters affecting the reported results.

## 2 Input data

| **Dataset** | **Role and content** | **Version or snapshot** | **File**                   |
| ----------- | -------------------- | ----------------------- | -------------------------- |
| <Name>      | <Description>        | <Version>               | [Parquet](<relative-path>) |

## 3 Results

### 3.1 <Result title>

<Briefly explain the finding and its relevance.>

![<Description of the figure>](figures/<filename>.png)

<Caption explaining the figure and any relevant limitations.>

[Supporting table (CSV)](tables/<filename>.csv)

### 3.2 <Result title>

<Add further findings, figures or small Markdown tables as needed.>

## 4 Created datasets

| **Dataset** | **Content and intended use** | **Files**                                           |
| ----------- | ---------------------------- | --------------------------------------------------- |
| <Name>      | <Description>                | [CSV](<relative-path>) > [Parquet](<relative-path>) |

## 5 Validation and limitations

- Relevant checks and their outcomes.
- Failed checks and their consequences.
- Data-quality issues, uncertainty and interpretation limits.
- Restrictions on using the results in subsequent phases.

## 6 Summary and handoff

- Main findings and decisions.
- Completion status against the phase criteria.
- Unresolved issues and next actions.
- Outputs required by the next phase.
```

Include only results and artifacts belonging to the reported run. Explain when an expected output is unavailable or not applicable. A completed execution does not by itself establish that the phase's methodological completion criteria have been met.
