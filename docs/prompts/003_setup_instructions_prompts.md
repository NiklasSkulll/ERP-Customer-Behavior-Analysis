<div align="center">

# Prompts used for creating the setup documenation

[![GPT-6 Astra](https://img.shields.io/badge/GPT--6%20Astra-OpenAI%20model-%23352898?style=flat&labelColor=%2315934E)](https://developers.openai.com/api/docs/models/gpt-6-astra)

</div>

## Table of Contents

- [Prompts to create the MCP Serena setup documentation](#prompts-to-create-the-mcp-serena-setup-documentation)
    - [Initial prompt to create the first setup information](#initial-prompt-to-create-the-first-setup-information)
    - [Prompt used for development](#prompt-used-for-development)
- [Prompts for the documentation to create raw Python files](#prompts-for-the-documentation-to-create-raw-python-files)
    - [Initial prompt to create the first steps](#initial-prompt-to-create-the-first-steps)
    - [Prompt used for development](#prompt-used-for-development-1)
    - [Prompt used for updating the documentation](#prompt-used-for-updating-the-documentation)
- [Prompt for the documentation to manage the uv environment](#prompt-for-the-documentation-to-manage-the-uv-environment)
- [Prompt for the documentation to handle Git LFS](#prompt-for-the-documentation-to-handle-git-lfs)
- [Bibliography](#bibliography)

---

## Prompts to create the MCP Serena setup documentation

> This setup `docs/setup/mcp_serena_setup.md` got created all in one chat.

### Initial prompt to create the first setup information

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
I am working on a project for data analysis with Python and Jupyter notebooks. I want to use MCP Serena in this repo.

**What I need:**
- A good and simple onboarding / setup for Serena for my repo.
- Look at the documentation (https://oraios.github.io/serena/02-usage/050_configuration.html#agent-interfaces) and project (https://github.com/oraios/serena) and help me with it.

**Like:** a step-by-step plan with WSL commands. **Then:** What should a good config file look. I want MCP Serena for the understanding of my python and notebook scripts (if notebooks are supported) and my markdown documentation files, maybe for graphics and tables as well (if it is supported).

Maybe my workflow files help.
```

### Prompt used for development

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is a prompt that got used to improve and develop the MCP setup documentation. After that, the setup got improved and reviewed step-by-step.

**Prompt:**
```markdown
I give you my project description for my repo as context as well.

**Important:** I dont want any productive informations for the productive data in my repo. Please update the MCP Serena config with this new context.
```

---

## Prompts for the documentation to create raw Python files

> This setup `docs/setup/create_raw_python_files.md` got created all in one chat. The same chat got used in which the MCP Serena setup was created.

### Initial prompt to create the first steps

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
Now the setup for MCP Serena is finished.

**Next Step:**
We talked about the conversion of the Jupyter notebooks to raw Python mirror files. Now we need to document this setup as well.

**What we do now:**
- _Look and analyse in official documentations:_
  - How should we do it?
  - Is it a tool, that does the conversion? Is it in WSL/Linux via bash command or a Python script/command.
  - What is the exact Workflow and doing here?
```

### Prompt used for development

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

> Below is a prompt that got used to improve and develop the setup documentation for creating Python mirror files. After that, the setup got improved and reviewed step-by-step.

**Prompt:**
```markdown
I thought we'd say we don't need Jupytext?
[...]
And is it possible to have the output file a different name?
For e.g.: `01_Phase.ipynb` has the `01_Phase_mirror.py` as mirror raw Python file.
[...]
Can you give me the command for creating a `.venv` for the "ERP-Customer-Behavior-Analysis" project and the command for activate and deactivate it? In addition, I use uv and these files (see screenshot).
```

### Prompt used for updating the documentation

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
**Topic:** GitHub-Repo, Programming, Data-Analysis-Repo with Python and Jupyter notebooks.

**Task:** I have a documentation of how to convert notebooks to raw python files. The setup documentation is now out-dated, because I created a script, which does this conversion. Analyse both files and provide an update version of the documentation file in chat.

After that, tell me what changed and why
```

---

## Prompt for the documentation to manage the uv environment

> This setup `docs/setup/manage-uv-environment.md` got created in the same chat as [Prompt used for updating the documentation](#prompt-used-for-updating-the-documentation).

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
Ok, now look at the `create_raw_python_files.md` file again.

I moved the "manage uv" section into a new file `manage-uv-environment.md`:
- Look at it and analyse it.
- Provide me the missing header overview text. And if it needs improvement, improve it.
```

---

## Prompt for the documentation to handle Git LFS

> This setup `docs/setup/git_lfs_setup_handling.md` got created in the same chat as [Prompt for the documentation to manage the uv environment](#prompt-for-the-documentation-to-manage-the-uv-environment).

**AI model (model name (source)):**
- GPT-6 Astra (OpenAI, 2026c)

**Prompt:**
```markdown
Ok, we are now finished with this setup. I wanted to add git lfs for my CSV/Parquet files and Notebooks.

I have a setup for this in an other repo of mine. Can I use it? Or is it not up-to-date?

# Git LFS setup

Git LFS (Large File Storage) stores big files outside normal git history and keeps a tiny pointer file in the repo. This keeps clones fast and avoids bloating the git history.

**One‑time setup (WSL):**
sudo apt install git-lfs
git lfs install

**Per‑repo setup:**
git lfs track "*.csv"             # track large CSVs
git lfs track "*.ipynb"           # optional: large notebooks
git add .gitattributes            # commit tracking rules

**Then just use git normally:**
git add data/raw/*.csv
git commit -m "data: add raw datasets"
git push

**Useful commands:**
git lfs ls-files
git lfs status
git lfs pull

> **Key note for collaborators:** install git‑lfs before cloning, otherwise they get pointer files instead of the real datasets.
```

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
