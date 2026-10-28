"""Public example paths, independent of machine or environment variables."""

from ._base import AnalysisConfig, PROJECT_ROOT


CONFIG = AnalysisConfig(
    data_dir=PROJECT_ROOT / "data" / "data-example",
    output_dir=PROJECT_ROOT / "outputs" / "exports",
    is_production=False,
)
