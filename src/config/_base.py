"""Shared configuration type and repository location; no filesystem writes."""

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class AnalysisConfig:
    """Explicit input and output locations for one analysis environment.

    Importing a configuration does not read data or create directories.
    Append paths such as "raw/orders.parquet" or "figures/plot.png" to these
    roots. Notebook code creates the output subdirectories it needs.
    """

    data_dir: Path
    output_dir: Path
    is_production: bool
