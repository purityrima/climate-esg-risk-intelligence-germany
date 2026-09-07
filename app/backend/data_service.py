from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = PROJECT_ROOT / "data" / "processed"
MODEL_ROOT = PROJECT_ROOT / "notebooks" / "models"


@st.cache_data(show_spinner=False)
def load_registry() -> pd.DataFrame:
    path = DATA_ROOT / "registry" / "NCRR_Germany_district_median_1990_2025.csv"
    return pd.read_csv(path, dtype={"district_code": "string"})


@st.cache_data(show_spinner=False)
def load_master_data() -> pd.DataFrame:
    path = DATA_ROOT / "master" / "master289_dataset_1990_2025.csv"
    return pd.read_csv(path, dtype={"district_code": "string"})

@st.cache_data(show_spinner=False)
def load_annual_registry() -> pd.DataFrame:
    path = (
        PROJECT_ROOT
        / "notebooks"
        / "data"
        / "processed"
        / "registry"
        / "NCRR_Germany_1990_2025.csv"
    )
    return pd.read_csv(path, dtype={"district_code": "string"})

@st.cache_data(show_spinner=False)
def load_map_geojson() -> dict:
    path = DATA_ROOT / "registry" / "NCRR_Germany_district_median_1990_2025.geojson"
    with path.open(encoding="utf-8") as file:
        geojson = json.load(file)

    colours = {
        "Low": [199, 224, 158, 230],
        "Medium": [255, 193, 94, 230],
        "High": [255, 99, 99, 230],
    }
    for feature in geojson["features"]:
        props = feature["properties"]
        risk_class = props.get("median_risk_class")
        props["fill_colour"] = colours.get(risk_class, [180, 186, 194, 230])
        props["display_name"] = props.get("district_name") or props.get("NUTS_NAME") or "District"
        props["display_score"] = (
            f"{props['median_predicted_rcrs']:.2f}"
            if props.get("median_predicted_rcrs") is not None
            else "Not modelled"
        )
        props["display_class"] = risk_class or "Not modelled"
    return geojson


@st.cache_data(show_spinner=False)
def load_json_artifact(filename: str) -> dict:
    with (MODEL_ROOT / filename).open(encoding="utf-8") as file:
        return json.load(file)


@st.cache_data(show_spinner=False)
def load_test_predictions() -> pd.DataFrame:
    return pd.read_csv(MODEL_ROOT / "test_predictions.csv")


@st.cache_data(show_spinner=False)
def load_shap_importance() -> pd.DataFrame:
    path = MODEL_ROOT / "shap" / "global_shap_feature_importance.csv"
    return pd.read_csv(path)
