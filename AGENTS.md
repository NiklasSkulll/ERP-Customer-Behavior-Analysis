<!-- MANUAL -->
<div align="center">

# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

**Instructions for AI agents working on this project:** Keep it brief and follow conventions. See [BACKLOG.md](BACKLOG.md) for open tasks.

## Shift Handoff (ALWAYS read this first)

**Before each new session:** _First_, read this `AGENTS.md`. _Afterward_, read [HANDOVER.md](HANDOVER.md) (the top entry) in its entirety. It contains the status of the last session, the next planned step, decisions made along with their rationale and potential pitfalls. _After that_, consult the [BACKLOG.md](BACKLOG.md) (Task Status) and MCP Serena-Memory files (in [.serena/](.serena/)).

> **Important notes for development:**
>- For notebook-related changes, _edit only_ the source notebooks in [src/notebooks/](src/notebooks/). Python files in [src/raw-notebooks/](src/raw-notebooks/) are _read-only mirrors_ of notebook code. Use them for navigation and inspection only. Never edit, overwrite, regenerate, delete or synchronize these mirror files. Their generation is handled separately by the user. If a mirror differs from its source notebook, treat the notebook as authoritative and report the mismatch.
>- Never inspect, load, search, execute against or modify production data located [src/.notebooks/](src/.notebooks/), [data/data-prd/](data/data-prd/) and [outputs/.exports/](outputs/.exports/). Do not copy production information into chat responses, code examples, documentation, handovers or Serena memories. If a task requires production access, stop and request a synthetic reproduction or data-free specification.

**At the end of the session:** _First_, add a new entry at the top of [HANDOVER.md](HANDOVER.md). A template is provided at the bottom of this `AGENTS.md`. _Afterward_, update the [BACKLOG.md](BACKLOG.md). _At the end_, update relevant Serena memories using its memory operations. Run onboarding only for initial setup or when a deliberate refresh is needed.

</div>

<!-- END MANUAL -->

---

<!-- AUTO-MANAGED: project-description -->
## Overview

- This repository supports a bachelor's thesis on detecting, typing and explainably describing changes in B2B wholesale customers' purchasing behaviour using ERP order data. It is a research project; an end-to-end analysis pipeline and evaluation results are not yet implemented.
- The [project plan](docs/project/bachelor_thesis_project_plan.md) is the source of truth for objectives, scope, candidate measures and evaluation commitments. The [FUUCCE framework](docs/framework/fuucce_framework.md) operationalises it; the completed [data description](docs/project/data_description.md) defines the available tables, fields and mappings.
- FUUCCE has six phases: Familiarise and assess → Use data and prepare profiles → Uncover and characterise changes → Construct the taxonomy → Classify and explain → Evaluate and discuss.
- The plan covers a 24-month window, with time-window profile comparison as the main detection direction. Ordering activity, net order value and assortment form the core; discounts are optional. Profitability analysis, churn prediction and causal explanations are outside scope.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: build-commands -->
## Build & Development Commands

Run commands from the repository root. Python is selected by [.python-version](.python-version) (3.12); [pyproject.toml](pyproject.toml) requires Python >=3.12 and uv >=0.13.1. Use the existing `.venv/bin/python` for checks to avoid incidental dependency installation.

| Command | Purpose |
| ------- | ------- |
| `bash setup/initial_setup.sh` | Contributor bootstrap: prepares tools, Git hooks, Git LFS and the environment; changes local configuration and may install/download dependencies. |
| `bash setup/initial_setup.sh --check` | Inspect setup status; exit code `1` means setup is incomplete. |
| `uv sync --locked` | Synchronize the environment with the committed lockfile. |
| `PYTHONPATH="$PWD/src" uv run --locked jupyter lab` | Launch Jupyter with `src/config` importable as `config`; use the project interpreter. |
| `.venv/bin/python -B setup/csv_to_parquet.py --help` | Inspect CSV converter usage without processing data. |
| `.venv/bin/python -B setup/notebook_to_raw_python.py --help` | Inspect exporter usage; mirror generation remains exclusively user-managed. |
| `.venv/bin/python -B setup/create_documentation_site.py --help` | Inspect documentation generator usage without building. |
| `bash -n setup/initial_setup.sh` | Check Bash syntax without running setup. |
| `uv --no-cache lock --check --offline` | Check lockfile consistency without resolving dependencies online. |
| `git diff --check` | Check changes for whitespace errors. |

The user-facing documentation build command is `uv run --locked python setup/create_documentation_site.py`. It replaces `docs/docsite/`. **Agents must build in an isolated copy of allowed public Markdown sources or synthetic fixtures:** the current generator traverses the repository before filtering exclusions, so running it in the real checkout would traverse protected directories.

There is no configured automated test, lint or type-check suite. Use checks appropriate to the change; do not claim that a project-wide suite passed. Do not execute notebooks, convert datasets or run bootstrap as a routine verification step.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: architecture -->
## Architecture

- [docs/project/](docs/project/) contains the authoritative plan and data schema; [docs/framework/](docs/framework/) contains the methodological workflow. [README.md](README.md) is the project entry point.
- [docs/literature/](docs/literature/) contains research notes and bibliography; [docs/prompts/](docs/prompts/) records historical AI prompts. Preserve original prompt text when updating navigation or annotations.
- [setup/](setup/) contains the Bash bootstrap and standalone Python utilities for CSV conversion, notebook export and documentation generation. There is no installed application package or deployment service.
- [src/config/](src/config/) contains the frozen `AnalysisConfig` type and explicit example/production profiles. Paths derive from the repository location; imports perform no data reads or directory creation.
- [src/notebooks/](src/notebooks/) contains authoritative public notebooks. [src/raw-notebooks/](src/raw-notebooks/) contains user-generated mirrors for read-only navigation. Both currently contain placeholders.
- Example inputs and intermediate datasets belong under `data/data-example/` (`raw/`, `interim/`, `processed/`); public synthetic artifacts belong under `outputs/exports/`. Production roots remain subject to the restrictions above.
- [docs/docsite/](docs/docsite/) is generated output. Its generator and shared CSS live in [setup/create_documentation_site.py](setup/create_documentation_site.py). Local thesis sources in `docs/.bachelor-thesis/` and literature originals in `docs/literature/.literature-source-files/` are ignored and excluded from conversion.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: conventions -->
## Code Conventions

- Follow existing utility structure: `argparse`, `pathlib`, paths rooted at `__file__`, `main() -> int`, and `raise SystemExit(main())`. Load third-party dependencies after argument parsing so `--help` remains data-free.
- Preserve temporary-file/build-directory writes and replacement behaviour; do not replace them with partial in-place output writes.
- Public notebooks explicitly import `from config.example import CONFIG`. Only user-managed private copies select production. Use `CONFIG.data_dir` and `CONFIG.output_dir`; avoid machine detection, environment-based profile switching and hard-coded absolute paths.
- Prepared CSV tables use UTF-8, comma separators and English uppercase columns. Preserve ERP field meanings and use the plan's measure names, such as `ORDERCOUNT` and `TOTALORDERVALUE`, and identifiers `CUSTOMERID` and `PERIODSTART`.
- Load tabular inputs from Parquet; export new or updated datasets to CSV, convert to Parquet, retain both and verify schema/missing-value preservation. Preserve original extracts.
- Keep Markdown source authoritative, preserve established title wrappers and tables of contents, and check link case and anchors. Update generator styling rather than editing generated HTML/CSS manually.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: patterns -->
## Detected Patterns

- Explicit configuration keeps the same analysis code usable on development and production PCs. Switching profiles is a deliberate import change in a private notebook copy, not an automatic fallback.
- Order headers repeat across item rows: count distinct eligible orders and include each order-level net amount once. Distinguish missing coverage from inactivity and leave zero-denominator averages/shares undefined.
- Candidate detection, taxonomy development, automatic assignment and explanation are separate steps. Preserve supporting observations and represent combined changes, ambiguity and insufficient evidence explicitly.
- Development is iterative; final evaluation uses reserved evidence. Fix measures, thresholds, taxonomy criteria and description rules before final evaluation, and report sensitivity analyses separately.
- The documentation preprocessor handles centred Markdown wrappers and list separators. Link rewriting maps converted Markdown to HTML, preserves queries/fragments, and sends other local targets to GitHub `main`; folder links ending in `/` use the folder view.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: git-insights -->
## Git Insights

- Existing commits use Conventional Commit titles, for example `fix(docsite): ...` and `chore(docs): ...`. Keep changes focused and use the [pull request template](.github/pull_request_template.md) to explain motivation, results and validation.
- CSV and Parquet files use Git LFS through [.gitattributes](.gitattributes). Do not replace LFS pointers or download datasets merely to inspect repository structure.
- [.githooks/pre-commit](.githooks/pre-commit) rejects tracked/staged paths under the three production roots. It checks paths, not notebook contents; saved outputs can still expose production information in public files.
- The bootstrap activates repository-local hooks and existing LFS hooks. Do not reconfigure the user's Git setup as an incidental check.
- Inspect working-tree and staged changes before editing; preserve unrelated work and staged state. Keep `pyproject.toml` and `uv.lock` together when intentionally changing dependencies. Do not commit or push unless requested.

<!-- END AUTO-MANAGED -->

---

<!-- AUTO-MANAGED: best-practices -->
## Best Practices

- Use focused source inspection and Serena navigation; confirm the active project before memory or symbol writes. Never use broad searches, indexing or traversal that enters protected production paths.
- Verify that any execution requires no data or uses explicitly fully synthetic fixtures. A directory named `data-example` alone does not establish synthetic provenance; pseudonymized real records are not synthetic.
- For utility changes, use isolated temporary fixtures. For documentation changes, check links, anchors and generated output as relevant. Report checks actually run and their limitations.
- Known tooling limits: the CSV converter scans immediate `data/data-example/*.csv`, whereas documented extracts are under `raw/`; the docsite converter assumes repository-root-relative links and its generated heading IDs differ from some GitHub-style anchors. Do not silently assume these cases work.
- Describe recorded net order values accurately; do not equate them with realised revenue. Descriptions explain observed changes and assignment evidence, not customer motives. Without a user study, factual correctness and traceability do not demonstrate user comprehensibility or usefulness.
- Keep durable technical guidance in Serena memories, session history in HANDOVER.md and task status in BACKLOG.md, subject to explicit user overrides. Do not copy historical claims into current guidance without verifying them against the plan and source files.

<!-- END AUTO-MANAGED -->

<!-- MANUAL -->
## Template for a HANDOVER.md-Entry

Copy and paste this template below for the next entry in [HANDOVER.md](HANDOVER.md).

```markdown
## YYYY-MM-DD - <AI model name>: <Short Overview-Title>

### Session Summary
- 2–4 bullets summarizing the goal, outcome, and overall state of the session.

### Changes & Findings
- Implemented ...
- Refactored ...
- Commit `abc1234`: ...
- Investigated X and determined that ...
- Discovered that Y depends on ...

### End-Session Status
- Branch / Push Status / HEAD Hash
- Working Tree Status
- Build Status
- App launchability
- Other conditions relevant to the next session

### Next Step
- Specific, with reference to the backlog or code location.

### Important Decisions with Justification
- What was decided + WHY.
- The "why" is the most important part. The "what" can be read by the successor in the code.

### Gotchas and Pitfalls
- What had to be worked around?
- What else might come as a surprise?

### Modified and new Memories
- Serena / Auto-Memory, with a brief explanation of why it was saved.

### Open or Unresolved
- What's in the backlog, what remains a question mark, what was deliberately postponed.
```
<!-- END MANUAL -->
