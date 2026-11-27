"""Check the locked analysis and notebook tools using invented inputs only."""

import asyncio
from html.parser import HTMLParser
import importlib
import os
import tempfile
import unittest
from unittest.mock import patch


class ExportedHTML(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.images = []
        self.focusable = 0
        self.text = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img":
            self.images.append(attrs)
        if attrs.get("tabindex") == "0":
            self.focusable += 1

    def handle_data(self, data):
        self.text.append(data)


class DependencyCompatibilityTests(unittest.TestCase):
    def test_analysis_and_jupyter_dependencies_import_together(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(
            os.environ, {"MPLBACKEND": "Agg", "MPLCONFIGDIR": folder}
        ):
            for name in (
                "duckdb", "markdown", "numpy", "pandas", "pyarrow", "scipy",
                "sklearn", "ruptures", "matplotlib", "seaborn", "plotly.express",
                "jupyterlab.labapp", "jupyter_server.serverapp", "ipykernel.kernelapp",
            ):
                with self.subTest(module=name):
                    importlib.import_module(name)

    def test_tornado_event_loop_runs_an_async_task(self):
        from tornado.ioloop import IOLoop

        async def task():
            await asyncio.sleep(0)
            return "completed"

        loop = IOLoop(make_current=False)
        try:
            self.assertEqual(loop.run_sync(task), "completed")
        finally:
            loop.close(all_fds=True)

    def test_notebook_exports_preserve_code_and_html_without_execution(self):
        import nbformat
        from nbconvert import HTMLExporter, PythonExporter

        # Executing this code would fail. Exporters must only render saved cells.
        source = 'raise RuntimeError("This cell must not execute")'
        notebook = nbformat.v4.new_notebook(
            metadata={"language_info": {"name": "python"}},
            cells=[
                nbformat.v4.new_markdown_cell("# Fixture report\n\n**Invented** findings.", id="intro"),
                nbformat.v4.new_code_cell(
                    source, id="code", execution_count=1,
                    outputs=[nbformat.v4.new_output("display_data", data={
                        "text/plain": "Invented result",
                        "text/html": '<p>Invented result</p><img src="data:image/png;base64,AA==">',
                    })],
                ),
            ],
        )
        before = nbformat.writes(notebook)
        python, _ = PythonExporter().from_notebook_node(notebook)
        html, _ = HTMLExporter().from_notebook_node(notebook)
        self.assertIn(source, python)
        parsed = ExportedHTML(html)
        text = " ".join(parsed.text)
        self.assertIn("Fixture report", text)
        self.assertIn("Invented result", text)
        self.assertEqual(len(parsed.images), 1)
        self.assertTrue(parsed.images[0].get("alt"))
        self.assertGreaterEqual(parsed.focusable, 2)
        self.assertEqual(nbformat.writes(notebook), before)


if __name__ == "__main__":
    unittest.main()
