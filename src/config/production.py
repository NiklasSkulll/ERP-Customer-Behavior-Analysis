"""Private analysis paths; import only from notebooks in src/.notebooks/."""

from ._base import AnalysisConfig, PROJECT_ROOT


CONFIG = AnalysisConfig(
    data_dir=PROJECT_ROOT / "data" / "data-prd",
    output_dir=PROJECT_ROOT / "outputs" / ".exports",
    is_production=True,
)
