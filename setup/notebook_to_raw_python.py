"""Convert saved project notebooks to Python mirror files without executing cells. Requires nbconvert: uv add --dev nbconvert"""

import argparse
import os
from pathlib import Path
import sys
import tempfile

def main() -> int:
    # Require exactly one conversion mode. --help is provided by argparse
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument(
        "--all-files", action="store_true",
        help="Convert all notebooks recursively, excluding .ipynb_checkpoints.",
    )
    selection.add_argument(
        "--file", type=Path, metavar="NOTEBOOK",
        help="Convert one .ipynb file. Relative paths are relative to src/notebooks. Absolute paths must be inside that directory.",
    )
    args = parser.parse_args()

    # Resolve project paths relative to this script, not the working directory
    project_root = Path(__file__).resolve().parent.parent
    source_dir = (project_root / "src" / "notebooks").resolve()
    target_dir = project_root / "src" / "raw-notebooks"
    if not source_dir.is_dir():
        parser.exit(status=1, message=f"Error: Directory does not exist: {source_dir}\n")

    # Validate explicit input before importing the conversion dependency
    if args.file is not None:
        source = args.file if args.file.is_absolute() else source_dir / args.file
        source = Path(os.path.abspath(source))

        try:
            resolved_source = source.resolve()
        except (OSError, RuntimeError) as exc:
            parser.error(f"Could not resolve notebook path: {exc}")

        if not source.is_relative_to(source_dir) or not resolved_source.is_relative_to(source_dir):
            parser.error(f"Notebook must be inside: {source_dir}")

        if ".ipynb_checkpoints" in source.relative_to(source_dir).parts:
            parser.error("Notebook checkpoints cannot be exported.")

        if source.suffix != ".ipynb" or not source.is_file():
            parser.error(f"Expected an existing .ipynb file: {source}")

        sources = [source]
    else:
        try:
            sources = sorted(
                path
                for path in source_dir.rglob("*.ipynb")
                if path.is_file()
                and ".ipynb_checkpoints" not in path.relative_to(source_dir).parts
            )
        except OSError as exc:
            parser.exit(status=1, message=f"Error: Could not find notebooks: {exc}\n")

        if not sources:
            parser.exit(status=1, message=f"Error: No notebooks found in: {source_dir}\n")

    # Delay third-party imports so --help works without nbconvert installed
    try:
        from nbconvert import PythonExporter
    except ImportError:
        parser.exit(status=1, message="Error: Missing dependency. Install it with: uv add --dev nbconvert\n")

    try:
        exporter = PythonExporter()
    except Exception as exc:
        parser.exit(status=1, message=f"Error: Could not initialize nbconvert: {exc}\n")

    converted = 0
    failures = 0
    for source in sources:
        relative_path = source.relative_to(source_dir)
        target = target_dir / relative_path.with_name(f"{source.stem}_mirror.py")
        temp_target = None

        try:
            # Reject links or '..' paths that would escape the configured trees
            if not source.resolve().is_relative_to(source_dir):
                raise ValueError(f"Notebook resolves outside {source_dir}")
            if not target.parent.resolve().is_relative_to(target_dir.absolute()):
                raise ValueError(f"Output directory resolves outside {target_dir}")

            # This exports saved cells. It does not execute them or save the notebook
            python_code, _ = exporter.from_filename(str(source))
            target.parent.mkdir(parents=True, exist_ok=True)

            # Use a unique sibling temporary file and close it before replacement. Failed writes leave the old mirror intact
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", newline="\n",
                dir=target.parent, prefix=f".{target.name}.", suffix=".tmp",
                delete=False,
            ) as handle:
                temp_target = Path(handle.name)
                handle.write(python_code)
            temp_target.replace(target)
        except Exception as exc:
            failures += 1
            print(f"Failed: {relative_path}: {exc}", file=sys.stderr)
        else:
            converted += 1
            print(f"Converted: {relative_path} -> {target.relative_to(target_dir)}")
        finally:
            if temp_target is not None:
                try:
                    temp_target.unlink(missing_ok=True)
                except OSError as exc:
                    print(f"Could not remove temporary file '{temp_target}': {exc}", file=sys.stderr)

    print(f"Converted: {converted}; failed: {failures}. Output: {target_dir}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
