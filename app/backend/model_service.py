from __future__ import annotations

from .data_service import load_json_artifact


def model_summary() -> dict:
    """Return deployment-safe model metadata without loading the training stack."""
    metadata = load_json_artifact("model_metadata.json")
    metrics = load_json_artifact("performance_metrics.json")
    thresholds = load_json_artifact("risk_thresholds.json")
    return {"metadata": metadata, "metrics": metrics, "thresholds": thresholds}
