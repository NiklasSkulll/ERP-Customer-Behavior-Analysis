"""Build documentation exclusively from invented Markdown in temporary trees."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "create_documentation_site.py"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = Counter()
        self.links = {}
        self.stylesheets = []
        self.code = []
        self.in_code = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links[attrs["href"]] = attrs
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs["href"])
        if tag == "code":
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == "code":
            self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.code.append(data)


class DocumentationSiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "setup").mkdir()
        self.script = self.root / "setup/create_documentation_site.py"
        shutil.copyfile(SCRIPT, self.script)
        self.site = self.root / "docs/docsite"

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def build(self):
        result = subprocess.run(
            [sys.executable, "-B", str(self.script)], cwd=self.root,
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def page(self, name):
        return Document((self.site / "pages" / name).read_text(encoding="utf-8"))

    def test_ordered_and_unordered_lists_after_labels_and_in_blockquotes(self):
        cases = {
            "ordered": ("**Steps:**\n1. First\n2. Second", "ol", False),
            "multidigit": ("**Steps:**\n10. First\n11. Second", "ol", False),
            "quoted_ordered": ("> Steps:\n>1. First\n>2. Second", "ol", True),
            "quoted_spaced_ordered": ("> **Steps:**\n> 1. First\n> 2. Second", "ol", True),
        }
        for name, marker in (("dash", "-"), ("plus", "+"), ("star", "*")):
            cases[name] = (f"**Steps:**\n{marker} First\n{marker} Second", "ul", False)
            cases[f"quoted_{name}"] = (f"> Steps:\n>{marker} First\n>{marker} Second", "ul", True)
        for name, (source, _, _) in cases.items():
            self.write(f"{name}.md", source)
        self.build()
        for name, (_, tag, quoted) in cases.items():
            with self.subTest(case=name):
                page = self.page(f"{name}.html")
                self.assertEqual(page.tags[tag], 1)
                self.assertEqual(page.tags["li"], 2)
                self.assertEqual(page.tags["blockquote"], int(quoted))

    def test_internal_navigation_and_external_targets_preserve_urls(self):
        self.write("README.md", """# Overview

[Other](docs/second.md?view=full#details)
[Spaced name](docs/Other%20page.md)
[Heading](#overview)
[Web](https://example.com/page.html)
[Protocol relative](//example.com/page.html)
[Script](setup/tool.py)
[Folder](src/config/)

<a href="#overview" target="_blank">Raw heading</a>
""")
        self.write("docs/second.md", "# Details")
        self.write("docs/Other page.md", "# Other")
        self.build()
        page = self.page("README.html")
        for href in ("../index.html", "second.docs.html?view=full#details",
                     "Other%20page.docs.html", "#overview"):
            with self.subTest(href=href):
                self.assertEqual(page.links[href]["target"], "_self")
        for href in (
            "https://example.com/page.html", "//example.com/page.html",
            "https://github.com/NiklasSkulll/ERP-Customer-Behavior-Analysis/blob/main/setup/tool.py",
            "https://github.com/NiklasSkulll/ERP-Customer-Behavior-Analysis/tree/main/src/config",
        ):
            with self.subTest(href=href):
                self.assertEqual(page.links[href]["target"], "_blank")
                self.assertTrue({"noopener", "noreferrer"} <= set(page.links[href]["rel"].split()))
        index_html = (self.site / "index.html").read_text(encoding="utf-8")
        index = Document(index_html)
        self.assertEqual(index.tags["li"], 3)
        self.assertEqual(index.links["pages/README.html"]["target"], "_self")
        self.assertEqual(index.links["pages/second.docs.html"]["target"], "_self")
        self.assertLess(index_html.index("Root"), index_html.index("docs/"))

    def test_centered_markdown_tables_and_code_examples_are_preserved(self):
        source = """<div align="center">

# Fixture title

**Introductory text.**

</div>

| Column | Value |
| ------ | ----- |
| A | 1 |

```markdown
**Steps:**
1. First
2. Second
```

    **Quoted label:**
    >1. Example
"""
        path = self.write("example.md", source)
        self.build()
        page = self.page("example.html")
        self.assertEqual(page.tags["h1"], 1)
        self.assertEqual(page.tags["strong"], 1)
        self.assertEqual(page.tags["table"], 1)
        self.assertEqual(page.tags["pre"], 2)
        self.assertEqual(page.tags["ol"], 0)
        self.assertIn("**Steps:**\n1. First\n2. Second", "".join(page.code))
        self.assertIn("**Quoted label:**\n>1. Example", "".join(page.code))
        self.assertEqual(page.stylesheets, ["../style.css"])
        self.assertTrue((self.site / "style.css").read_text(encoding="utf-8").strip())
        self.assertEqual(path.read_text(encoding="utf-8"), source)

    def test_excluded_fixture_directories_do_not_produce_pages(self):
        self.write("README.md", "# Allowed")
        # All directories below are invented fixtures inside this test's /tmp tree.
        for folder in (
            ".git", ".venv", "node_modules", "data/data-prd", "src/.notebooks",
            "outputs/.exports", "docs/.bachelor-thesis", "docs/literature/.literature-source-files",
        ):
            self.write(f"{folder}/excluded.md", "# Excluded fixture")
        self.build()
        self.assertEqual([p.name for p in (self.site / "pages").iterdir()], ["README.html"])

    def test_rebuild_replaces_stale_pages_after_a_complete_build(self):
        old = self.write("old.md", "# Old fixture")
        self.build()
        self.assertTrue((self.site / "pages/old.html").exists())
        old.unlink()
        self.write("new.md", "# New fixture")
        self.build()
        self.assertFalse((self.site / "pages/old.html").exists())
        self.assertTrue((self.site / "pages/new.html").is_file())
        self.assertFalse((self.root / "docs/docsiteTEMP").exists())


if __name__ == "__main__":
    unittest.main()
