<div align="center">

# Prompts used for setting up this GitHub-Repo

[![GPT-6 Astra](https://img.shields.io/badge/GPT--6%20Astra-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-astra)

</div>

## Table of Contents

- [Prompts to create the pre-commit hook](#prompts-to-create-the-pre-commit-hook)
- [Prompts to setup the repo](#prompts-to-setup-the-repo)
    - [Prompt to clean up the headings and links from the tables of content](#prompt-to-clean-up-the-headings-and-links-from-the-tables-of-content)
    - [Prompt to update and write the README.md](#prompt-to-update-and-write-the-readmemd)
    - [Prompt to analyse the Git LFS setup and setup the uv environment](#prompt-to-analyse-the-git-lfs-setup-and-setup-the-uv-environment)
    - [Prompt to setup MCP Serena for this project](#prompt-to-setup-mcp-serena-for-this-project)
- [Prompt to clean up the repo](#prompt-to-clean-up-the-repo)
- [Prompt to create the pull request template](#prompt-to-create-the-pull-request-template)
- [Prompt to improve the project plan](#prompt-to-improve-the-project-plan)
- [Bibliography](#bibliography)

---

## Prompts to create the pre-commit hook

> The pre-commit `.githooks/pre-commit` hook got created all in one chat.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> An existing chat with a question about the `.gitignore` file was used to create this hook (see initial prompt below).

**Initial Prompt:**
```markdown
**Topic:** GitHub/Git/Programming

**Task:** I am setting up a repo, where I anaylse big data with Python in Jupyter notebooks. Below is my current `.gitignore` file. Do I need for this repo additions in my `.gitignore`? If so, which and why?

# Production notebooks and python files
src/.notebooks/

# Production data and all derived artifacts stored here
data/data-prd/
outputs/.exports/

# Logging files
*.log

# Environments
.env
.venv
env/.env
venv/
ENV/.env

# MCP: Serena
.serena/cache/
.serena/logs/
.serena/project.local.yml
```

**Prompt to create this hook:**
```markdown
I wanted a clear structure and have a `env/.env` and `env/.env.example` file.

**This below would ignore the env example file:**
- `env/`
- `ENV/`

Thats why I wrote `env/.env` and `ENV/.env`.

**And these Folders shouldn't be pushed. NEVER:**
- `src/.notebooks/`
- `data/data-prd/`
- `outputs/.exports/`

Is there a way to make sure this never happens? Like, e.g. with a pre-commit hook? If so, how can I add such a precommit hook check?
```

---

## Prompts to setup the repo

> This clean up got done in one chat.

### Prompt to clean up the headings and links from the tables of content

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

**Prompt:**
```markdown
Look at my whole project and analyse it so you got the context. This isnt a GitHub repo yet. We need to make some clean-up for the initial push.
1. Analyse the repo so that you know everything. Ignore the AGENTS.md instructions for now.
2. Then look at all my table of contents links/missing links and their wording. Correct the wording if its wrong and create the missing GitHub-Style links for the headings. DONT change ANYTHING ELSE.
```

### Prompt to update and write the README.md

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

**Prompt:**
```markdown
Now, Look at my README.md Its quiet empty. Improve it with the current best pratices. Use links to setup, docs if nessessary
```

### Prompt to analyse the Git LFS setup and setup the uv environment

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

**Prompt:**
```markdown
Like this .gitattributes? If so. Help me set up my uv. Look at my doc (uv and python is installed), and tell me in chat what commands do I need and what packages do I ned to add for my repo? Look at my project (like pandas, or plotly for diagrams) what would I need and what do I need for my scripts to work. ALl this can I now set up
```

### Prompt to setup MCP Serena for this project

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

**Prompt:**
```markdown
No I dont have notebooks yet. But the setup is nice. Now look at my serena mcp setup docu. I ned to setup my repo with it now and run the index/onboarding. Tell me in chat aswell: What commands do I need to do?
```

---

## Prompt to clean up the repo

> The same chat as the initial setup file got created in [004_setup_files_creation_prompts.md](docs/prompts/004_setup_files_creation_prompts.md#prompt-to-create-a-initial-start-script), was used for this clean up.

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

> The config files in `src/config` (`src/config/__init__.py`, `src/config/_base.py`, `src/config/example.py` and `src/config/production.py`) got created with this prompt and follow up iteration.

**Prompt:**
```markdown
**Great now, lets focus one these, step-by-step:**
- _Several details need fixing alongside the script:_
    - All five hooks are tracked as 100644. **->** What do I need to choose/do here, or is it covered by the initial setup file?
    - The notebook conversion guide uses scripts/ instead of setup/ **->** Update this guide
    - env/.env.example is empty, so creating a local .env currently provides no benefit.
    - No minimum uv version is declared. **->** is this important? If so, lets choose my current version, or? Can we declare this?
    - The README incorrectly says dependency files are empty and recommends Python 3.11. **->** we do this later, like the serena correction
```

---

## Prompt to create the pull request template

> The template `.github/pull_request_template.md` got created all in one chat.

**AI model (model name (source)):**
- GPT-6.1 Sol (Codex)

**Prompt:**
```markdown
**I have a new improvement to make:**
- Analyse my repo, if you haven't got the context yet (you can use Serena MCP for it).
- Analyse the current best practices for writing pull request in GitHub.

**What I want:**
- Look at my `.github/pull_request_template.md` now.
- This is currently empty.
- Create a best practice and for my project the best/fitting pull request template.
```

---

## Prompt to improve the project plan

> This improvement got done in one chat. The file `docs/project/bachelor_thesis_project_plan.md` got created here.

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is an example prompt that got used to improve and finalise the project plan step-by-step after it got reviewed each time.

**Prompt:**
```markdown
**Role - You are an expert in:**
- Academic writing, academic reviewer, professor of computer science, and the scope of bachelor's theses
- Expert in data analysis using Python and notebooks

**Topic:** Bachelor's thesis in computer science, GitHub/programming, project planning, data analysis

**Task:** I would like to adjust and refine/improve my project plan for my bachelor's thesis. Since I now have the ERP data I want to analyze—and have also removed some items due to the scope of the project—I need to adjust the plan accordingly. I have created a public repository for the methodological section of my thesis ([https://github.com/NiklasSkulll/ERP-Customer-Behavior-Analysis](https://github.com/NiklasSkulll/ERP-Customer-Behavior-Analysis)).

**For context and information:**
- Open and analyze the GitHub project (README.md, project-related documentation, sample data feature structure (currently only column names), dataset documentation)
- Open and analyze the `docs/project/complete_project_plan1.md` file.

First, read and analyze everything; further instructions will follow. The goal is to have a finished plan. However, we'll take it step by step here and begin once you've analyzed and read everything.
```

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
