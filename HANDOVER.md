<div align="center">

# HANDOVER.md

**Convention for every agent working with this `HANDOVER.md`:**

Instructions for the **start of a session** can be found under _`## Shift Handoff` in [AGENTS.md](AGENTS.md)_.

**At the end of a session**, carefully read the instructions under _`## Shift Handoff` in [AGENTS.md](AGENTS.md)_ and use the template under _`## Template for a HANDOVER.md-Entry` in [AGENTS.md](AGENTS.md)_ to create a new entry in this file.

**Important:** Do not delete old entries, because they represent the history, like a git log, but in narrative form. If the file becomes too long, move the oldest entries to [HANDOVER_ARCHIVE.md](HANDOVER_ARCHIVE.md) (once there are more than 50 entries).

</div>

---

## 2026-10-28 - GPT-6: Initial Serena onboarding

### Session Summary
- Activated the requested ERP-Customer-Behavior-Analysis project in Serena and performed initial onboarding.
- Reviewed agent instructions, setup documentation, dependency configuration, utility scripts, and methodology/schema documentation. Production directories were not inspected; no notebooks or datasets were executed or generated.
- Verified Python symbol lookup and Markdown heading navigation through Serena; prepared concise project memories.

### Changes & Findings
- Python 3.12.3 is installed in `.venv`; `.python-version` pins 3.12 and `pyproject.toml` requires >=3.12. Analysis and notebook dependencies are populated.
- All three `setup/*.py` files passed AST parsing and `--help` execution with the project interpreter; DuckDB, Markdown, and nbconvert imported successfully.
- Serena located `main` in `setup/csv_to_parquet.py` and `MCP Serena setup/Setup/Onboarding` in the setup guide.
- README still describes empty dependency files and Python 3.11 in its getting-started text; record correction in BACKLOG.md.
- Converter scans immediate CSV files in `data/data-example/`, whereas schema documentation uses `data/data-example/raw/`; no data was inspected to resolve this mismatch.

### End-Session Status
- Git is not initialized locally: no branch, HEAD, push, or Git working-tree status is available.
- Public notebook and mirror directories contain only `.gitkeep`; no analysis entry point or results exist yet.
- Data-free checks passed; no analysis/build or dataset conversion was attempted. No test/lint/type-check configuration is declared in pyproject.toml.
- HANDOVER.md and BACKLOG.md updated; Serena memories describe the confirmed setup and boundaries.

### Next Step
- Address the documentation/path-alignment tasks in BACKLOG.md before starting synthetic notebook development.

### Important Decisions with Justification
- Treat installed configuration as authoritative over stale README text to avoid repeating environment setup.
- Keep onboarding limited to navigation, metadata, syntax, and CLI-help checks because no analysis notebooks exist and production access is prohibited.

### Gotchas and Pitfalls
- Serena reports the requested mixed-case project path; this WSL workspace is exposed with a lowercase path. Avoid assuming a second checkout exists based on spelling alone.
- Notebook mirror generation is exclusively user-managed. Never run the exporter beyond `--help` as an agent.
- The documentation generator rebuilds its output directory and discovers Markdown recursively; its build was not run during onboarding.

### Modified and new Memories
- `core`: source map, research workflow, and project boundaries.
- `tech_stack`: environment, dependencies, and Jupyter interpreter selection.
- `suggested_commands`: actual utility commands and execution restrictions.
- `conventions`: notebook authority, data formatting, and script conventions.
- `task_completion`: data-free validation and required session closeout order.

### Open or Unresolved
- Correct stale README setup instructions and align CSV input paths.
- Jupyter kernel selection in the user's editor has not been observed; select the project `.venv/bin/python`.
- End-to-end analysis, evaluation results, and a project license remain absent. No Git initialization or push was requested.
