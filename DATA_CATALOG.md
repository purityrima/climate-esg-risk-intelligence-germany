# Data Catalog

## Project Overview

This catalog describes the datasets used and generated throughout the AI Climate & ESG Risk Intelligence Platform for Multi-Sector Decision Support in Germany.

The project integrates climate hazard, socioeconomic, administrative boundary, and machine learning datasets to produce Regional Climate Risk Scores (RCRS), the National Climate Risk Registry for Germany (NCRR-G), and the Germany Climate Risk Map.

---

# 1. Raw Climate Datasets

| Dataset | Source | Spatial Unit | Period | Description |
|---------|---------|--------------|--------|-------------|
| Heatwave Days | Copernicus ERA5 | NUTS-2 | 1990–2025 | Annual heatwave intensity |
| Flood Proxy (Rx5day) | Copernicus ERA5 | NUTS-2 | 1990–2025 | Maximum 5-day precipitation |
| Drought Magnitude | Copernicus ERA5 | NUTS-2 | 1990–2025 | Annual drought severity |

---

# 2. Raw Socioeconomic Datasets

| Dataset | Source | Spatial Unit | Period | Description |
|---------|---------|--------------|--------|-------------|
| GDP per Capita | INKAR | District | 1990–2025* | Economic capacity indicator |
| Unemployment Rate | INKAR | District | 1990–2025* | Socioeconomic vulnerability indicator |

*Missing years were imputed during preprocessing.

---

# 3. Administrative Datasets

| Dataset | Source | Purpose |
|---------|---------|---------|
| NUTS-3 Boundaries (2024) | Eurostat GISCO | National mapping |
| Administrative Crosswalk | Project-generated | Harmonize NUTS identifiers |
| NUTS-2 → NUTS-3 Area Weights | Project-generated | Spatial interpolation |

---

# 4. Processed Datasets

| Dataset | Description |
|---------|-------------|
| heatwave_project400_1990_2025.csv | Harmonized heatwave dataset |
| rx5day_project400_1990_2025.csv | Harmonized flood dataset |
| drought_project400_1990_2025.csv | Harmonized drought dataset |
| gdp_per_capita_inkar_1990_2025.csv | Harmonized GDP dataset |
| unemployment_inkar_1990_2025.csv | Harmonized unemployment dataset |
| master_dataset_1990_2025.csv | Integrated master dataset |
| master289_dataset_1990_2025.csv | Complete-case modelling dataset |

---

# 5. Machine Learning Outputs

| Output | Description |
|---------|-------------|
| Regional Climate Risk Score (RCRS) | Continuous predicted climate risk score |
| Risk Classes | Low, Medium and High climate risk |
| SHAP Values | Global and local model explainability |
| Trained FFNN | Final neural network model |
| Preprocessing Pipeline | Saved preprocessing workflow |

---

# 6. Registry Outputs

| Output | Description |
|---------|-------------|
| NCRR_Germany_district_registry.csv | National Climate Risk Registry |
| NCRR_Germany_district_registry.parquet | Registry (Parquet) |
| NCRR_Germany_district_median_1990_2025.geojson | Spatial registry for mapping |

---

# 7. Map Outputs

| Output | Description |
|---------|-------------|
| germany_climate_risk_map_median_1990_2025.png | National Climate Risk Map |

---

# 8. Data Processing Workflow

1. Download climate datasets
2. Download socioeconomic datasets
3. Harmonize administrative boundaries
4. Spatially interpolate climate variables
5. Harmonize socioeconomic indicators
6. Merge datasets
7. Create complete-case modelling dataset
8. Engineer features
9. Train FFNN
10. Generate RCRS
11. Produce NCRR-G
12. Produce Germany Climate Risk Map

---

# Notes

- Climate data originate from Copernicus ERA5.
- Administrative boundaries originate from Eurostat GISCO.
- Socioeconomic indicators originate from the INKAR Regional Database.
- Results are intended for research, education, and climate risk decision support.