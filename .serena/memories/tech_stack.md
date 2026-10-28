# Environment
- WSL/Linux; uv-managed non-package project. Python requirement >=3.12 in pyproject.toml; `.python-version` pins 3.12. Project `.venv/bin/python` verified as CPython 3.12.3 at onboarding. Resolve current versions from pyproject.toml/uv.lock rather than README, which still has stale bootstrap text.
- Runtime dependencies: duckdb, markdown, pandas, numpy, pyarrow, scipy, scikit-learn (import sklearn), ruptures, matplotlib, seaborn, plotly[express].
- Dev group: nbconvert, jupyterlab, ipykernel, anywidget. SHAP is optional in the research plan and not declared.
- Jupyter: select project `.venv/bin/python` in the editor; installation does not prove UI kernel selection. Launch via `uv run --locked jupyter lab`. No notebooks yet.
- Serena is a separately installed tool (2.0.0 observed); do not add it to project dependencies. Project uses LSP python+markdown and REPL interface; exclusions in .serena/project.yml apply in addition to .gitignore.
- Python symbol and Markdown nested-heading lookup were both verified through Serena.
- `.gitattributes` tracks CSV/Parquet with LFS; notebooks currently use ordinary Git. Pre-commit guard exists but requires Git initialization and hook configuration. Git was not initialized at onboarding.