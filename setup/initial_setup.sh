#!/usr/bin/env bash
# Contributor bootstrap for Ubuntu/Debian and WSL. Safe to rerun.
# Run with Bash; no Python installation is needed to start.
set -Eeuo pipefail

ASSUME_YES=0
CHECK_ONLY=0
USE_COLOR=1
STAGE='Checking setup'
INSTALLER=''
GREEN='' YELLOW='' RED='' BLUE='' RESET=''
HOOK_NAMES=(pre-commit pre-push post-checkout post-commit post-merge)

usage() {
    cat <<'EOF'
Usage: bash setup/initial_setup.sh [--check | --yes] [--no-color]

  No options    Inspect installed tools, then show the setup menu.
  --check       Report setup status without changing anything; exit 1 if incomplete.
  --yes         Run recommended setup and approve missing-tool installations.
                Conflicting custom Git hooks still require interactive approval.
  --no-color    Disable colors (also respects NO_COLOR and redirected output).
  -h, --help    Show this help.

Recommended setup activates the existing Git hooks locally, configures Git LFS,
downloads LFS files for the current revision, and synchronizes the locked Python
environment including Jupyter. Existing compatible tools are reused.

Automatic system-package installation supports Ubuntu/Debian, including WSL.
Other Linux distributions can use existing tools or install missing tools manually.
Serena and editor configuration remain optional: see docs/setup/mcp_serena_setup.md.
EOF
}

message() {
    local color="$1" label="$2"
    shift 2
    printf '%b[%s]%b %s\n' "$color" "$label" "$RESET" "$*"
}

die() {
    message "$RED" ERROR "$*" >&2
    exit 1
}

cleanup() {
    if [[ -n "$INSTALLER" && -f "$INSTALLER" ]]; then
        rm -f -- "$INSTALLER"
    fi
}

on_error() {
    local status="$?"
    message "$RED" ERROR "$STAGE failed (exit $status). Fix the error above and rerun this script." >&2
    exit "$status"
}

confirm() {
    local answer
    if (( ASSUME_YES )); then
        message "$BLUE" INFO "$1 [approved by --yes]"
        return 0
    fi
    printf '%s [y/N] ' "$1"
    IFS= read -r answer || die 'No input received; setup stopped. Use --yes for unattended setup.'
    case "$answer" in
        y|Y|yes|YES) return 0 ;;
        *) return 1 ;;
    esac
}

step() {
    STAGE="$1"
    printf '\n'
    message "$BLUE" STEP "$STAGE"
}

install_package() {
    local package="$1" distro=''
    if [[ -r /etc/os-release ]]; then
        distro=$(. /etc/os-release; printf '%s' "${ID:-}")
    fi
    case "$distro" in
        ubuntu|debian) ;;
        *) die "Install $package using your system package manager, then rerun setup. Automatic package installation supports Ubuntu/Debian." ;;
    esac
    command -v apt-get >/dev/null 2>&1 || die "apt-get is unavailable; install $package manually."
    confirm "Install missing system package '$package' with apt-get (may require sudo)?" || die "Install $package manually, then rerun setup."
    if (( EUID == 0 )); then
        apt-get update
        apt-get install -y "$package"
    else
        command -v sudo >/dev/null 2>&1 || die "sudo is unavailable; ask your administrator to install $package."
        sudo apt-get update
        sudo apt-get install -y "$package"
    fi
}

find_python() {
    command -v uv >/dev/null 2>&1 &&
        uv --no-cache python find --no-python-downloads "$PYTHON_VERSION" >/dev/null 2>&1
}

show_status() {
    local hook configured missing=0
    printf '\nRepository: %s\nPython target: %s (from .python-version)\n\n' "$REPO_ROOT" "$PYTHON_VERSION"
    message "$GREEN" OK "$(git --version) ($(command -v git))"
    if git lfs version >/dev/null 2>&1; then
        message "$GREEN" OK "$(git lfs version)"
    else
        message "$YELLOW" MISSING 'Git LFS'
        missing=1
    fi
    if command -v uv >/dev/null 2>&1; then
        message "$GREEN" OK "$(uv --version) ($(command -v uv))"
        if find_python; then
            message "$GREEN" OK "Python $PYTHON_VERSION: $(uv --no-cache python find --no-python-downloads "$PYTHON_VERSION")"
        else
            message "$YELLOW" MISSING "Python $PYTHON_VERSION discoverable by uv"
            missing=1
        fi
    else
        message "$YELLOW" MISSING 'uv (setup can install uv and then Python)'
        missing=1
    fi
    configured=$(git config --local --get core.hooksPath || true)
    if [[ "$configured" == '.githooks' ]]; then
        message "$GREEN" OK 'Local Git hooks: .githooks'
    else
        message "$YELLOW" PENDING "Local Git hooks: ${configured:-not configured}"
        missing=1
    fi
    for hook in "${HOOK_NAMES[@]}"; do
        if [[ ! -x ".githooks/$hook" ]]; then
            message "$YELLOW" PENDING "Executable hook: .githooks/$hook"
            missing=1
        fi
    done
    if [[ -x .venv/bin/python ]]; then
        message "$BLUE" INFO "Existing environment: $(.venv/bin/python --version 2>&1)"
        # Read package metadata only; do not synchronize or import analysis packages.
        if ! .venv/bin/python -B - "$PYTHON_VERSION" <<'PY'
import importlib.metadata
import sys

target = tuple(map(int, sys.argv[1].split('.')))
if sys.version_info[:len(target)] != target:
    raise SystemExit(1)
for package in ('duckdb', 'markdown', 'matplotlib', 'numpy', 'pandas', 'plotly',
                'pyarrow', 'ruptures', 'scikit-learn', 'scipy', 'seaborn',
                'anywidget', 'ipykernel', 'jupyterlab', 'nbconvert'):
    try:
        importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        raise SystemExit(1)
PY
        then
            message "$YELLOW" PENDING 'Environment needs synchronization with the project Python and dependencies.'
            missing=1
        fi
    else
        message "$YELLOW" PENDING 'Project .venv'
        missing=1
    fi
    STATUS_INCOMPLETE="$missing"
}

configure_hooks() {
    step 'Activate existing Git hooks locally'
    local hook configured hooks_dir conflict=0
    configured=$(git config --get core.hooksPath || true)
    if [[ -n "$configured" && "$configured" != '.githooks' && "$configured" != "$REPO_ROOT/.githooks" ]]; then
        message "$YELLOW" WARN "An existing hooksPath would be replaced: $configured"
        conflict=1
    elif [[ -z "$configured" ]]; then
        hooks_dir=$(git rev-parse --git-path hooks)
        for hook in "$hooks_dir"/*; do
            [[ -f "$hook" && -x "$hook" && "$hook" != *.sample ]] || continue
            if ! cmp -s "$hook" ".githooks/${hook##*/}"; then
                message "$YELLOW" WARN "An existing hook would be bypassed: $hook"
                conflict=1
            fi
        done
    fi
    if (( conflict )); then
        (( ! ASSUME_YES )) || die 'Custom hooks detected. Rerun interactively to approve switching to .githooks.'
        confirm 'Switch this repository to .githooks? Existing custom hook files will be kept.' || die 'Hook configuration left unchanged.'
    fi
    for hook in "${HOOK_NAMES[@]}"; do
        [[ -f ".githooks/$hook" ]] || die "Missing existing hook: .githooks/$hook"
    done
    # Repair permissions in this checkout, including clones with 100644 hook modes.
    # This does not stage files or change their contents.
    for hook in "${HOOK_NAMES[@]}"; do
        chmod u+x ".githooks/$hook"
        [[ -x ".githooks/$hook" ]] || die "Cannot make .githooks/$hook executable. Check filesystem permissions."
    done
    git config --local core.hooksPath .githooks
    message "$GREEN" OK 'Existing pre-commit guard and LFS hooks activated for this repository.'
}

configure_lfs() {
    step 'Configure Git LFS and download files for the current revision'
    if ! git lfs version >/dev/null 2>&1; then
        install_package git-lfs
        git lfs version
    fi
    # The repository already provides the LFS hooks; keep those files intact.
    git lfs install --local --skip-repo
    message "$BLUE" INFO 'Downloading current-revision LFS content; repository access and network connectivity are required.'
    message "$BLUE" INFO 'If download fails, check remote access, missing uploaded objects, LFS limits and any configured download filters.'
    git lfs pull
    message "$GREEN" OK 'Git LFS configured; current-revision download completed using your LFS filters.'
}

ensure_uv() {
    if command -v uv >/dev/null 2>&1; then
        return
    fi
    confirm 'Install uv in ~/.local/bin using the official Astral installer (shell profiles stay unchanged)?' || die 'Install uv manually, then rerun setup.'
    if ! command -v curl >/dev/null 2>&1 && ! command -v wget >/dev/null 2>&1; then
        install_package curl
    fi
    INSTALLER=$(mktemp)
    if command -v curl >/dev/null 2>&1; then
        curl --fail --silent --show-error --location https://astral.sh/uv/install.sh --output "$INSTALLER"
    else
        wget -q https://astral.sh/uv/install.sh -O "$INSTALLER"
    fi
    UV_INSTALL_DIR="$HOME/.local/bin" UV_NO_MODIFY_PATH=1 sh "$INSTALLER"
    export PATH="$HOME/.local/bin:$PATH"
    command -v uv >/dev/null 2>&1 || die 'uv installation finished but uv is unavailable on PATH.'
    message "$GREEN" OK "Installed $(uv --version)"
    message "$BLUE" INFO 'For future shells, ensure ~/.local/bin is on PATH: export PATH="$HOME/.local/bin:$PATH"'
}

configure_python() {
    step 'Prepare uv and the project Python environment'
    ensure_uv
    if ! find_python; then
        confirm "Install Python $PYTHON_VERSION with uv?" || die "Python $PYTHON_VERSION is required; install it and rerun setup."
        uv python install "$PYTHON_VERSION"
    fi
    if [[ -d .venv ]]; then
        message "$BLUE" INFO 'Synchronizing existing .venv; uv may replace an incompatible interpreter and remove undeclared packages.'
        confirm 'Synchronize the existing project environment?' || die 'Existing environment left unchanged.'
    fi
    message "$BLUE" INFO 'Installing dependencies from uv.lock, including Jupyter and development tools.'
    message "$BLUE" INFO 'If uv cannot read the project or lockfile, update uv using its original installation method and retry.'
    uv sync --locked --python "$PYTHON_VERSION"
    step 'Verify the Python environment'
    uv run --locked --no-sync --python "$PYTHON_VERSION" python -c '
import sys
import duckdb, markdown, matplotlib, numpy, pandas, plotly, pyarrow
import ruptures, sklearn, scipy, seaborn, anywidget, ipykernel, jupyterlab, nbconvert
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Analysis and Jupyter imports: OK")
'
    message "$GREEN" OK 'Locked Python environment and Jupyter are ready.'
}

main() {
    local choice do_lfs=1 do_python=1
    for choice in "$@"; do
        case "$choice" in
            --check) CHECK_ONLY=1 ;;
            --yes) ASSUME_YES=1 ;;
            --no-color) USE_COLOR=0 ;;
            -h|--help) usage; return ;;
            *) usage >&2; die "Unknown option: $choice" ;;
        esac
    done
    if (( CHECK_ONLY && ASSUME_YES )); then
        die 'Choose either --check or --yes.'
    fi
    if [[ -t 1 && -z "${NO_COLOR+x}" && "${TERM:-}" != dumb ]] && (( USE_COLOR )); then
        GREEN=$'\033[32m' YELLOW=$'\033[33m' RED=$'\033[31m' BLUE=$'\033[36m' RESET=$'\033[0m'
    fi
    trap cleanup EXIT
    trap on_error ERR
    [[ "$(uname -s)" == Linux ]] || die 'Run this script on Linux or inside WSL. Native Windows and macOS setup are not automated.'
    command -v git >/dev/null 2>&1 || die 'Git is required. Install Git and clone the repository before running setup.'
    REPO_ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
    cd -- "$REPO_ROOT"
    [[ "$(git rev-parse --show-toplevel)" == "$REPO_ROOT" ]] || die 'Run this script from its original setup/ directory inside the cloned repository.'
    # Keep uv overrides from redirecting exact synchronization to another project
    # or a shared environment. These changes affect this script's process only.
    unset UV_PROJECT UV_WORKING_DIR
    export UV_PROJECT_ENVIRONMENT="$REPO_ROOT/.venv"
    [[ -s .python-version && -s pyproject.toml && -s uv.lock ]] || die 'Missing .python-version, pyproject.toml or uv.lock. Restore the committed setup files.'
    PYTHON_VERSION=$(tr -d '[:space:]' < .python-version)
    [[ "$PYTHON_VERSION" =~ ^[0-9]+\.[0-9]+(\.[0-9]+)?$ ]] || die 'Expected a Python major.minor or major.minor.patch version in .python-version.'
    printf '\nERP Customer Behavior Analysis — Contributor Setup\n'
    show_status
    if (( CHECK_ONLY )); then
        message "$BLUE" INFO 'Read-only check finished. This checks installed tools and package presence; it does not verify lockfile synchronization or remote LFS availability.'
        return "$STATUS_INCOMPLETE"
    fi
    if (( ! ASSUME_YES )); then
        printf '\n1) Recommended contributor setup\n2) Choose setup steps (existing hooks are always activated)\n3) Check only\n0) Exit\n\nChoose [1]: '
        IFS= read -r choice || die 'No input received; setup stopped. Use --yes for unattended setup.'
        case "${choice:-1}" in
            1) ;;
            2)
                confirm 'Configure Git LFS and download current-revision files?' || do_lfs=0
                confirm 'Prepare uv, Python and the locked Jupyter environment?' || do_python=0
                ;;
            3) return "$STATUS_INCOMPLETE" ;;
            0) return ;;
            *) die 'Invalid menu choice. Rerun and choose 0, 1, 2 or 3.' ;;
        esac
    fi
    configure_hooks
    if (( do_lfs )); then configure_lfs; fi
    if (( do_python )); then configure_python; fi
    printf '\n'
    if (( do_lfs && do_python )); then
        message "$GREEN" OK 'Setup complete.'
    else
        message "$GREEN" OK 'Selected setup steps complete; skipped steps may still be needed.'
    fi
    if (( do_python )); then
        printf '\nStart Jupyter from the repository root:\n  uv run --locked jupyter lab\n\nIn your editor, select:\n  %s/.venv/bin/python\n' "$REPO_ROOT"
    fi
    if (( ! do_lfs )); then
        message "$YELLOW" INFO 'LFS setup was skipped. The activated LFS hooks require Git LFS to be installed and configured.'
    fi
    printf '\nOptional Serena setup: docs/setup/mcp_serena_setup.md\n'
}

main "$@"
