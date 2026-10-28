<div align="center">

# Set up and use Git LFS

This guide explains how to install Git Large File Storage (Git LFS), configure tracking for CSV files, Parquet files and Jupyter notebooks and work with those files in the repository.

Git LFS stores file contents separately from ordinary Git objects and commits small pointer files to the repository. This reduces the growth of ordinary Git history when large files change. A normal clone still downloads the LFS files needed for the checked-out revision.

> The installation, tracking and file-handling commands follow the official Git LFS and GitHub documentation (GitHub, n.d.-a, n.d.-b; Git LFS,n.d.-a, n.d.-b, n.d.-c, n.d.-d).

</div>

## Table of Contents

- [Overview](#overview)
- [Install and initialize Git LFS](#install-and-initialize-git-lfs)
- [Configure repository tracking](#configure-repository-tracking)
- [Convert files already tracked by Git](#convert-files-already-tracked-by-git)
- [Commit the setup](#commit-the-setup)
- [Add or update files](#add-or-update-files)
- [Clone and retrieve LFS files](#clone-and-retrieve-lfs-files)
- [Useful commands](#useful-commands)
- [Storage and download usage](#storage-and-download-usage)
- [Bibliography](#bibliography)

---

## Overview

Git LFS is installed separately from the project.

Run repository-specific commands from the repository root. Git LFS tracking rules are stored in `.gitattributes`, which must be committed so collaborators use the same rules.

Tracking patterns select files by name or path, not by size. For example, `*.csv` matches small CSV files as well as large ones.

---

## Install and initialize Git LFS

**Install Git LFS on Ubuntu or Debian under WSL:**
```bash
sudo apt update
sudo apt install git-lfs
```

**Initialize Git LFS for your user account and check the installed version:**
```bash
git lfs install
git lfs version
```

Initialize Git LFS once per user account in each environment where you use Git. If you use both Windows Git and Git inside WSL, configure each environment separately.

Use a maintained version with current security fixes. Distribution packages may lag behind upstream releases. Consult the official installation instructions if you need a newer version.

---

## Configure repository tracking

**Track CSV and Parquet files:**
```bash
git lfs track "*.csv"
git lfs track "*.parquet"
```

**To also track all Jupyter notebooks:**
```bash
git lfs track "*.ipynb"
```

Keep the patterns quoted so the shell passes them unchanged to Git LFS. These extension patterns apply throughout the repository, including subdirectories. Tracking all notebooks is optional. Small, frequently edited notebooks can remain in ordinary Git.

**If only selected notebooks need LFS, use their paths instead of the `*.ipynb` rule:**
```bash
git lfs track "src/notebooks/01_Phase.ipynb"
```

Choose either the broad notebook rule or specific notebook paths according to the repository's needs.

Generated Python mirror files in `src/raw-notebooks` remain in ordinary Git unless separately configured for LFS.

**Review the tracking rules and stage them:**
```bash
git lfs track
git add .gitattributes
```

---

## Convert files already tracked by Git

Skip this section if none of the matching files are already tracked by Git. Adding tracking rules does not automatically convert every existing tracked file.

**To apply the rules to files in the current working tree, re-stage them:**
```bash
git add --renormalize .
```

**Start the setup with a clean working tree:** This command can also stage unrelated changes to tracked files and apply other attributes configured in the repository.

This operation prepares the current file versions for LFS storage in the next commit. It does not remove large file contents from earlier commits.

Moving historical versions into LFS requires a separate migration using `git lfs migrate`. Such a migration can rewrite commit history and should be planned with collaborators.

New, untracked files are not included by `--renormalize`; add them explicitly with `git add`.

---

## Commit the setup

**Review the staged changes and LFS status:**
```bash
git status
git diff --cached --stat
git lfs status
```

**Commit and push the tracking rules and any converted files:**
```bash
git commit -m "chore: configure Git LFS tracking"
git push
```

Git LFS uploads the required file contents as part of the normal push workflow.

---

## Add or update files

Save your datasets and notebooks, then use normal Git commands.

**Example - replace these paths with the files you want to commit:**
```bash
git add data/data-example/raw/example.csv
git add data/data-example/raw/example.parquet
git add src/notebooks/01_Phase.ipynb
```

**Review, commit and push:**
```bash
git lfs status
git diff --cached --stat
git commit -m "data: update datasets and analysis notebook"
git push
```

Files matching the committed LFS rules are stored through Git LFS. Other files are stored normally by Git.

---

## Clone and retrieve LFS files

**Collaborators should install Git LFS and run `git lfs install` before cloning:**
```bash
git lfs install
git clone <repository-url>
```

With automatic LFS downloads enabled, cloning retrieves the file contents needed for the checked-out revision.

**If a repository was cloned before Git LFS was configured and contains pointer files instead of actual datasets or notebooks, install Git LFS, then run these commands inside the repository:**
```bash
git lfs install
git lfs pull
```

`git lfs pull` downloads LFS content for the checked-out revision and updates the working files. It does not advance the branch to newer commits.

If content cannot be downloaded, check repository access, network connectivity, whether the LFS objects were uploaded and the repository owner's LFS usage limits.

---

## Useful commands

| **Command**        | **Purpose**                                                    |
| ------------------ | -------------------------------------------------------------- |
| `git lfs version`  | Show the installed Git LFS version.                            |
| `git lfs track`    | List configured tracking patterns.                             |
| `git lfs ls-files` | List LFS files in the current repository state.                |
| `git lfs status`   | Show LFS changes relevant to staging, committing, and pushing. |
| `git lfs pull`     | Download and check out LFS content for the current revision.   |

---

## Storage and download usage

GitHub applies separate storage and download allowances to Git LFS.

Each changed version of an LFS file counts as another complete file in storage. Small edits to a large dataset or notebook can therefore increase storage usage substantially.

Downloads count toward the repository owner's LFS bandwidth usage, including downloads by collaborators and automated workflows. Check the current GitHub allowances and billing settings before storing large or frequently regenerated datasets.

---

## Bibliography

See [docs/literature/Bibliography.md](docs/literature/Bibliography.md).
