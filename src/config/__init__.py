"""Explicit notebook configurations; importing this package selects no profile.

Public notebooks: ``from config.example import CONFIG``
Private notebooks: ``from config.production import CONFIG``

Make src importable when starting Jupyter from the repository root:
    PYTHONPATH="$PWD/src" uv run --locked jupyter lab
"""
