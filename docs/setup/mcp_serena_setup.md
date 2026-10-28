<div align="center">

# MCP Serena setup

**Serena** is an MCP server that helps AI coding assistants navigate, understand and edit this repository's Python code and Markdown documentation. This guide covers installation in WSL, project configuration, connecting AI clients and onboarding, including the notebook mirror workflow and production-data exclusions.

This guide draws on the official Serena repository and the documentation for Serena, Claude Code and Codex (Anthropic, n.d.a, n.d.b; OpenAI, n.d.; Oraios AI, 2026; Oraios AI & Oraios Software, n.d.a, n.d.b). The notebook mirror workflow, production-data exclusions and session instructions are project-specific adaptations.

</div>

## Table of Contents

- [Workflow](#workflow)
- [Installation](#installation)
- [Setup](#setup)
    - [Initialize MCP Serena](#initialize-mcp-serena)
    - [Prepare notebook mirrors](#prepare-notebook-mirrors)
    - [Index the project for MCP Serena](#index-the-project-for-mcp-serena)
    - [Connect an AI client](#connect-an-ai-client)
        - [Connect Codex CLI](#connect-codex-cli)
        - [Connect Claude Code](#connect-claude-code)
        - [Connect Codex via VSCode](#connect-codex-via-vscode)
        - [Connect Claude Code via VSCode](#connect-claude-code-via-vscode)
    - [Onboarding](#onboarding)
- [Configuration](#configuration)
- [Bibliography](#bibliography)

---

## Workflow

1. Initialize the project.
2. Apply the project configuration.
3. Check exclusions and prepare the Python mirrors.
4. Index the project.
5. Connect the AI client.
6. Perform onboarding.

---

## Installation

Run these commands inside WSL. Install `uv` first using its official installation instructions if it is not already available.

**Install Serena (Oraios AI & Oraios Software, n.d.b):**
```bash
uv tool install -p 3.13 serena-agent
serena init
serena --version
```

**For an existing installation, update Serena instead (Oraios AI & Oraios Software, n.d.b):**
```bash
uv tool upgrade serena-agent
serena --version
```

These instructions were validated with _Serena 2.0.0_ and _Python 3.13_.

---

## Setup

### Initialize MCP Serena

Before indexing or connecting an AI client, apply the settings in [Configuration](#configuration), including all production-data exclusions. If the configuration file for MCP Serena `.serena/project.yml` already exists, edit that file instead of initializing the project again. Merge the settings without duplicating YAML keys (Oraios AI & Oraios Software, n.d.b).

**Initialize MCP Serena in the project root (Oraios AI & Oraios Software, n.d.b):**
```bash
serena project create --name ERP-Customer-Behavior-Analysis --language python --language markdown
```

### Prepare notebook mirrors

- Source notebooks: `src/notebooks/`
- Read-only Python mirrors: `src/raw-notebooks/`
- Refresh mirrors using the repository's existing export workflow in [docs/setup/Create_raw_Python_files.md](docs/setup/Create_raw_Python_files.md) before initial indexing and after notebook changes.
- Keep `src/raw-notebooks/` accessible to Serena.
- Agents must not regenerate or edit mirrors.

The notebooks remain authoritative. Mirrors support Python navigation but do not provide access to notebook outputs or guarantee that every notebook cell is represented as a navigable symbol.

### Index the project for MCP Serena

**Index the project in the project root (Oraios AI & Oraios Software, n.d.b):**
```bash
serena project index
```

### Connect an AI client

Configure the AI client's MCP settings to launch the following executable with the arguments shown below. Replace USER and the repository path with their actual WSL values. After changing Serena's configuration, fully exit and reopen the CLI session. For the Codex VSCode extension, use Restart extension. Do not repeat registration for ordinary restarts.

#### Connect Codex CLI

**Register Serena once (OpenAI, n.d.):**
```bash
cd /home/USER/projects/ERP-Customer-Behavior-Analysis
codex mcp add serena -- /home/USER/.local/bin/serena start-mcp-server --project "$PWD" --context codex
```

**Check the registration and start Codex (OpenAI, n.d.):**
```bash
codex mcp list
codex
```

Inside Codex, enter `/mcp` to check the active server (OpenAI, n.d.).

#### Connect Claude Code

**Register Serena once (Anthropic, n.d.a):**
```bash
cd /home/USER/projects/ERP-Customer-Behavior-Analysis
claude mcp add --transport stdio --scope local serena -- /home/USER/.local/bin/serena start-mcp-server --project "$PWD" --context claude-code
```

**Start Claude Code (Anthropic, n.d.a):**
```bash
claude
```

Inside Claude Code, enter `/mcp` to check the active server (Anthropic, n.d.a).

#### Connect Codex via VSCode

**Setup from official source (OpenAI, n.d.):**
1. Open Codex Extension (`gear menu`), then go to `MCP servers - Add server`.
2. Select `STDIO`.
3. Enter information from table below.
4. Save, then select Restart extension. This is the documented extension-only setup.

| **Field**     | **Value**                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------ |
| **Name**      | `serena`                                                                                   |
| **Command**   | `/home/USER/.local/bin/serena`                                                             |
| **Arguments** | `start-mcp-server`, `--project`, your repository's absolute WSL path, `--context`, `codex` |

**Alternatively, edit `~/.codex/config.toml` inside WSL and add (OpenAI, n.d.):**
```toml
[mcp_servers.serena]
command = "/home/USER/.local/bin/serena"
args = [
  "start-mcp-server",
  "--project",
  "/home/USER/projects/ERP-Customer-Behavior-Analysis",
  "--context",
  "codex"
]
```

Use either the extension UI or the TOML configuration. If `[mcp_servers.serena]` already exists, update it instead of adding a duplicate. Replace the example repository path, save and restart the extension. Codex CLI is not required (OpenAI, n.d.).

#### Connect Claude Code via VSCode

**Setup from official source (Anthropic, n.d.b):**
1. Open the Claude Code extension.
2. Enter `/mcp` in its chat panel and select the option to add a server.
3. Select `STDIO` and enter the information below.
4. Choose project scope to save the configuration in the repository's `.mcp.json`.
5. Start a new conversation, enter `/mcp` and confirm that `serena` shows _Connected_.

| **Field**     | **Value**                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------ |
| **Name**      | `serena`                                                                                         |
| **Command**   | `/home/USER/.local/bin/serena`                                                                   |
| **Arguments** | `start-mcp-server`, `--project`, your repository's absolute WSL path, `--context`, `claude-code` |

Adding servers through the extension's `/mcp` dialog requires _Claude Code version 2.1.261 or later_ (Anthropic, n.d.b).

**Alternatively, create or edit `.mcp.json` in the repository root:**
```json
{
  "mcpServers": {
    "serena": {
      "type": "stdio",
      "command": "/home/USER/.local/bin/serena",
      "args": [
        "start-mcp-server",
        "--project",
        "/home/USER/projects/ERP-Customer-Behavior-Analysis",
        "--context",
        "claude-code"
      ]
    }
  }
}
```

Use either the extension UI or the JSON configuration. If `.mcp.json` already contains other servers, add `serena` to the existing `mcpServers` object without replacing those entries. Start a new conversation and approve the project MCP server if prompted. Enter `/mcp` to check the connection or reconnect Serena. If Serena was already registered through Claude Code CLI for this repository, use that existing registration instead of adding a duplicate. No separate CLI installation is required for the extension setup (Anthropic, n.d.a, n.d.b).

### Onboarding

Onboarding is performed by the connected AI agent using Serena, resulting in [.serena/memories/](.serena/memories/) files (Oraios AI & Oraios Software, n.d.b).

**Once connected, ask the agent to:**
> Onboard this repository using Serena. First follow the startup sequence in `AGENTS.md`. Inspect the project structure, dependency files, Python modules, notebooks and Markdown documentation. Do not execute notebooks or regenerate data.
>
> Identify the analysis environment and Jupyter kernel, data inputs, preprocessing steps, analysis entry points, outputs and existing validation commands. Distinguish confirmed facts from assumptions. Follow Serena's memory-maintenance instructions. Create concise memories covering the project overview, useful commands, analysis workflow and conventions. Reference `HANDOVER.md` and `BACKLOG.md` rather than duplicating their contents.
>
> Production data and production-derived artifacts are stored exclusively in `outputs/.exports/`, `src/.notebooks/`, and `data/data-prd/`. Do not inspect these directories. Notebooks in `src/notebooks/` contain no production data or production-derived outputs and may be inspected, including their saved outputs.
>
> Finish by reporting what you inspected, what remains unknown, and whether Python symbol navigation and Markdown heading navigation work.

---

## Configuration

**Change these properties (Oraios AI & Oraios Software, n.d.a):**
```yml
project_name: "ERP-Customer-Behavior-Analysis"

language_backend: LSP
language_servers:
  - python
  - markdown

agent_interface: REPL

encoding: "utf-8"
ignore_all_files_in_gitignore: true

ignored_paths:
  - "data/data-prd/**"
  - "outputs/.exports/**"
  - "src/.notebooks/**"
  - ".env"
  - "**/.env"
  - ".venv/**"
  - "venv/**"
  - "**/__pycache__/**"
  - "**/.ipynb_checkpoints/**"
  - ".serena/cache/**"
  - ".serena/logs/**"

read_only: false

initial_prompt: |
  This repository supports a bachelor's thesis on detecting,
  classifying and explaining changes in B2B wholesale customers'
  purchasing behavior using ERP-derived time series.

  Session workflow:
  - Read AGENTS.md first, then the newest HANDOVER.md entry in full,
    then BACKLOG.md and relevant Serena memories.
  - Report missing files or template-only sections honestly.
  - Follow AGENTS.md for end-of-session updates.
  - Store durable technical knowledge in Serena memories, session
    history in HANDOVER.md and task status in BACKLOG.md.

  Production-data boundary:
  - Never inspect, load, search, execute against, or modify
    data/data-prd/ or production data located elsewhere.
  - This also applies to production-derived profiles, aggregates,
    notebook outputs, plots, reports, logs, and model artifacts.
  - Do not copy production information into chat responses, code
    examples, documentation, handovers, or Serena memories.
  - Do not bypass exclusions through Python, shell commands,
    alternative tools, symlinks, or Git history.
  - Work only with code, approved data-free schema documentation,
    and explicitly identified fully synthetic fixtures.
  - Modified or pseudonymized real records are not fully synthetic.
  - If a task requires production access, stop and request a
    synthetic reproduction or data-free specification.
  - Production data and derived artifacts are stored exclusively in
    outputs/.exports/, src/.notebooks/ and data/data-prd/.
  - Notebooks in src/notebooks/ contain no production data or
    production-derived outputs. Their saved outputs may be inspected.

  Development:
  - Use Serena's tools for efficient Python and Markdown navigation,
    inspection and editing, subject to the file restrictions below.
  - When executing project scripts, tests or notebooks, use the project's
    configured Python environment or Jupyter kernel, even when execution
    is initiated through a Serena tool.
  - Before running code, confirm that it uses only explicitly identified
    fully synthetic inputs or requires no data, and cannot access
    production sources.
  - Do not execute notebooks or regenerate datasets during onboarding.

  Notebook editing:
  - For notebook-related changes, edit only the source notebooks in
    src/notebooks/.
  - Python files in src/raw-notebooks/ are read-only mirrors of notebook
    code. Use them for navigation and inspection only.
  - Never edit, overwrite, regenerate, delete or synchronize these mirror
    files. Their generation is handled separately by the user.
  - If a mirror differs from its source notebook, treat the notebook as
    authoritative and report the mismatch.
  - These rules do not authorize reading saved notebook outputs or
    embedded content derived from production data.
```

**Explanation of this configuration (Oraios AI & Oraios Software, n.d.a):**
- `agent_interface: REPL`: Lets the agent combine Serena operations in one call. It does not connect Serena to the Jupyter kernel.
- `read_only: false`: Allows normal editing and memory updates.
- `ignore_all_files_in_gitignore: true`: Ignores all files, which are defined in the `.gitignore`. Important ignores are defined under `ignored_paths` as well.
- Ignore rules filter Serena's project operations. They are not filesystem access controls. Likewise, the read-only mirror policy is an agent instruction, not a per-directory permission enforced by `read_only: false`.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
