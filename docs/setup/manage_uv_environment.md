<div align="center">

# Manage a Python environment with uv

This guide explains how to create and synchronize the project's Python environment, add development dependencies, and run commands within that environment using uv. Project dependencies are declared in `pyproject.toml`, while `uv.lock` records their resolved versions to support reproducible setup.

> The environment management commands follow the official uv documentation (Astral, n.d.).

</div>

## Table of Contents

- [Overview](#overview)
- [Create or synchronize the project environment](#create-or-synchronize-the-project-environment)
- [Add development dependencies](#add-development-dependencies)
- [Activation and deactivation](#activation-and-deactivation)
- [Bibliography](#bibliography)

---

## Overview

Run all commands from the repository root with uv installed.

**The project uses the following files and directory:**

| **File or directory** | **Purpose**                                          |
| --------------------- | ---------------------------------------------------- |
| `pyproject.toml`      | Declares project configuration and dependencies.     |
| `uv.lock`             | Records resolved dependency versions.                |
| `.venv`               | Contains the local Python environment managed by uv. |

Commit `pyproject.toml` and `uv.lock` to version control. Do not commit `.venv`.

---

## Create or synchronize the project environment

**Create `.venv` or synchronize an existing environment with the lockfile:**
```bash
uv sync --locked
```

The `--locked` option prevents lockfile updates. If `uv.lock` is missing or inconsistent with the project configuration, the command fails.

**If the dependency configuration was intentionally changed, update the lockfile:**
```bash
uv lock
```

Review the changes, then run `uv sync --locked` again. Commit any related changes to `pyproject.toml` and `uv.lock` together.

---

## Add development dependencies

Use `uv add --dev` to declare tools needed for development.

**For example, add `nbconvert` for notebook conversion if it is not already declared:**
```bash
uv add --dev nbconvert
```

This command updates `pyproject.toml`, updates `uv.lock` and synchronizes the project environment. Commit the configuration and lockfile changes together.

If the dependency is already declared, use `uv sync --locked` to install it from the existing lockfile.

---

## Activation and deactivation

Manual activation is unnecessary when using `uv run`.

**For example, start Python in the project environment with:**
```bash
uv run --locked python
```

This ensures the environment is synchronized before starting Python, without allowing lockfile updates. Alternatively, activate the environment to run commands such as `python` directly in the current shell.

**Activate on macOS or Linux using Bash or Zsh:**
```bash
source .venv/bin/activate
```

**Activate on Windows using PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Deactivate an activated environment:**
```text
deactivate
```

Activation changes which environment the shell uses. It does not install or synchronize dependencies. Run `uv sync --locked` beforehand.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
