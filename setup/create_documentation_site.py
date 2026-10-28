"""Convert project documentation Markdown files to HTML and combine to a documentation site."""

import os
import argparse
import shutil
from pathlib import Path
from html import escape
from urllib.parse import quote, unquote, urlsplit, urlunsplit

# Create a constant string containing the stylesheet
SITE_CSS = """
* {
    box-sizing: border-box;
}

html {
    background: #f3f5f7;
}

body {
    max-width: 960px;
    margin: 2rem auto;
    padding: clamp(1rem, 4vw, 3rem);
    background: #ffffff;
    color: #243042;
    font-family: system-ui, sans-serif;
    line-height: 1.7;
    overflow-wrap: anywhere;
    border-radius: 12px;
    box-shadow: 0 4px 24px #0000000a;
}

h1, h2, h3, h4 {
    color: #152238;
    line-height: 1.3;
    margin-top: 1.8em;
}

h1 {
    margin-top: 0;
}

h2 {
    padding-bottom: 0.3em;
    border-bottom: 1px solid #e2e8f0;
}

a {
    color: #175cd3;
    text-underline-offset: 0.2em;
}

a:hover {
    color: #123e8a;
}

a:focus-visible {
    outline: 2px solid #175cd3;
    outline-offset: 3px;
}

code {
    padding: 0.15em 0.35em;
    background: #eef2f6;
    border-radius: 4px;
    font-family: ui-monospace, monospace;
    font-size: 0.9em;
}

pre {
    padding: 1rem;
    overflow-x: auto;
    background: #eef2f6;
    border-radius: 8px;
}

pre code {
    padding: 0;
    background: transparent;
}

blockquote {
    margin-inline: 0;
    padding: 0.5rem 1rem;
    border-left: 4px solid #94a3b8;
    background: #f8fafc;
}

table {
    display: block;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    margin-block: 1.5rem;
}

th, td {
    padding: 0.65rem 1rem;
    border: 1px solid #dbe2ea;
    text-align: left;
}

th {
    background: #eef2f6;
}

img {
    max-width: 100%;
    height: auto;
}

hr {
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin-block: 2rem;
}
"""

def main() -> int:
    # Create argument parser and the argument '--help'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    # Resolve project root path, relative to this script
    project_root = Path(__file__).resolve().parent.parent

    # Resolve project doc paths as 'source_dir' and the 'target_dir' for the HTML results
    source_dir = project_root
    target_dir = project_root / "docs" / "docsite"
    build_dir = project_root / "docs" / "docsiteTEMP"
    if not source_dir.is_dir():
        parser.exit(status=1, message=f"Directory does not exist: {source_dir}\n")

    # Import HTML conversion package.
    try:
        import markdown
        from markdown.treeprocessors import Treeprocessor
    except ImportError:
        parser.exit(status=1, message="Missing dependency. Install it with: uv add markdown\n")

    # Exclude these directory names anywhere in the repository
    excluded_names = {".git", ".venv", "venv", "node_modules"}
    excluded_paths = {
        target_dir,
        build_dir,
        project_root / "outputs" / ".exports",
        project_root / "data" / "data-prd",
        project_root / "src" / ".notebooks",
    }

    sources = sorted(
        path
        for path in source_dir.rglob("*.md")
        if path.is_file()
        and not excluded_names.intersection(
            path.relative_to(source_dir).parts[:-1]
        )
        and not any(
            excluded in path.parents
            for excluded in excluded_paths
        )
    )

    # Start with an empty temporary build directory
    pages_dir = build_dir / "pages"
    try:
        if build_dir.exists():
            shutil.rmtree(build_dir)

        pages_dir.mkdir(parents=True)

    except OSError as exc:
        parser.exit(status=1, message=f"Error: Could not prepare '{build_dir}': {exc}\n")

    # Write the shared stylesheet for all generated pages
    stylesheet_path = build_dir / "style.css"
    try:
        stylesheet_path.write_text(SITE_CSS, encoding="utf-8")
    except OSError as exc:
        parser.exit(status=1, message=f"Error: Could not write stylesheet '{stylesheet_path}': {exc}\n")

    # Map each Markdown source to its generated HTML output path
    page_targets = {}
    for source in sources:
        relative_path = source.relative_to(source_dir)
        filename_parts = [relative_path.stem, *relative_path.parent.parts]
        filename = ".".join(filename_parts) + ".html"

        page_targets[source.resolve()] = pages_dir / filename

    # Adjust Markdown-generated links before rendering the final HTML
    class RepositoryLinkProcessor(Treeprocessor):
        def run(self, root):
            for link in root.iter("a"):
                href = link.get("href")
                if not href:
                    continue

                url = urlsplit(href)

                # Preserve external URLs and same-page section links
                if url.scheme or url.netloc or not url.path:
                    continue

                # The local links are relative to the repository root
                linked_source = (project_root / unquote(url.path).lstrip("/")).resolve()

                html_target = page_targets.get(linked_source)

                if html_target is not None:
                    # All generated document pages share the same folder
                    new_path = html_target.name
                else:
                    # Link to the original repository file or directory
                    new_path = Path(os.path.relpath(linked_source, pages_dir)).as_posix()

                    if url.path.endswith("/"):
                        new_path += "/"

                # Preserve any query string and section fragment.
                link.set("href", urlunsplit(("", "", quote(new_path), url.query, url.fragment)))

    # Convert each Markdown source into an HTML page
    index_entries = []
    for source in sources:
        relative_path = source.relative_to(source_dir)
        output_path = page_targets[source.resolve()]

        # Convert into HTML
        try:
            markdown_text = source.read_text(encoding="utf-8")

            converter = markdown.Markdown(
                extensions=["extra", "toc"],
            )
            converter.treeprocessors.register(
                RepositoryLinkProcessor(converter),
                "repository_links",
                1,
            )

            html_content = converter.convert(markdown_text)

            title = escape(source.stem)

            html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <nav aria-label="Site navigation">
        <a href="../index.html">Documentation overview</a>
    </nav>
    <main>
        {html_content}
    </main>
</body>
</html>
"""

            output_path.write_text(html_page, encoding="utf-8")

            page_url = quote(f"pages/{output_path.name}")
            label = escape(relative_path.as_posix())
            index_entries.append(f'<li><a href="{page_url}">{label}</a></li>')
        except (OSError, UnicodeError) as exc:
            parser.exit(status=1, message=f"Error: Could not convert '{source}' to '{output_path}': {exc}\n")

    print(f"Converted '{len(index_entries)}' Markdown files to HTML in '{pages_dir}'")

    # Build the overview from the successfully generated pages
    index_items = "\n".join(index_entries)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project documentation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Documentation of ERP-Customer-Behavior-Analysis</h1>
        <p>Browse the documentation for this repository.</p>
        <p>{len(index_entries)} documentation pages available:</p>
        <nav aria-label="Documentation pages">
            <ul>
                {index_items}
            </ul>
        </nav>
    </main>
</body>
</html>
"""

    index_path = build_dir / "index.html"

    try:
        index_path.write_text(index_html, encoding="utf-8")
    except OSError as exc:
        parser.exit(status=1, message=f"Error: Could not write index '{index_path}': {exc}\n")

    print(f"Index site created: {index_path}")

    # Remove the previous generated path for the documentation site and replace it with the generated 'build_dir'
    try:
        if target_dir.exists():
            shutil.rmtree(target_dir)

        build_dir.replace(target_dir)
    except OSError as exc:
        parser.exit(status=1,
            message=(
                f"Error: Could not replace '{target_dir}': {exc}\n"
                f"The completed build remains at '{build_dir}'\n"
            ),
        )

    print(
        f"Documentation site directory created: {target_dir}\n"
        f"Documentation site created: {target_dir / 'index.html'}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
