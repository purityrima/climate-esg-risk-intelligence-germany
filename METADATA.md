# Project Metadata

## Project Identification

- **Project title:** AI Climate Risk Intelligence Platform for Germany: Regional Climate Risk Prediction using Explainable Artificial Intelligence

- **Author:** Purity Rima Mbaabu

- **Role:** Full-Stack AI Engineer

- **Programme:** AI Engineering

- **Institution:** Digethic Business School, Germany

- **Submission date:** July 2026

- **Repository name:** climate-esg-risk-intelligence-germany

- **Project version:** Version 1.0

## Project Scope

- **Business problem:**
Develop an AI-powered climate risk intelligence platform capable of predicting regional climate risk for every German NUTS-3 district to support climate risk assessment, climate adaptation planning, banking applications, insurance analytics and public-sector decision making.

- **Research question:**
Can a Feed-Forward Neural Network accurately predict Regional Climate Risk Scores (RCRS) using climate hazard and socioeconomic indicators while providing transparent explanations through SHAP explainability?

- **Intended users:**
  - Banking institutions
  - Insurance companies
  - Government agencies
  - Climate adaptation planners
  - Researchers
  - Risk analysts

- **Geographic scope:** Germany (NUTS-3 administrative districts)

- **Temporal scope:** 1990–2025


## Dataset Metadata

- **Data sources:**
  - Copernicus ERA5 Climate Reanalysis
  - Eurostat GISCO
  - INKAR Regional Database

- **Variables:**
  - Heatwave Days
  - Flood Proxy (Rx5day)
  - Drought Magnitude
  - GDP per Capita
  - Unemployment Rate

- **Unit of observation:** District-Year

- **Number of observations (modelling dataset): 10,404** 10,404

- **Number of districts:** 289 (complete-case modelling dataset)

- **Analysis period:** 1990–2025

- **Spatial reference:** Germany NUTS-3

- **Data licences:** Original datasets remain subject to the licensing conditions of Copernicus, Eurostat GISCO and INKAR.

- **Data-processing summary:**
Climate datasets were harmonized from NUTS-2 to NUTS-3 using area-weighted spatial interpolation. Socioeconomic datasets were harmonized through an administrative crosswalk and temporally completed by imputing missing years. All datasets were merged into a complete-case modelling dataset used for FFNN development.

## Model Metadata

- **Baseline method:**
Regional Climate Risk Score (RCRS) construction using weighted climate and socioeconomic indicators.

- **Final method:**
Feed-Forward Neural Network (FFNN)

- **Framework:** PyTorch

- **Predictors:**
  - Heatwave Days
  - Flood Proxy (Rx5day)
  - Drought Magnitude
  - GDP per Capita
  - Unemployment Rate

- **Target variable:** Regional Climate Risk Score (RCRS)

- **Train/validation/test split:** 70% / 15% / 15%

- **Random seed:** 42

- **Evaluation metrics:** MAE, RMSE, R²

- **Explainability method:** SHAP (Global Feature Importance and Local Waterfall Explanation)

## Output Metadata

- **Regional Climate Risk Score:** Continuous predicted climate risk score (RCRS)

- **Risk classes:** Low, Medium and High climate risk based on validated thresholds

- **National Climate Risk Registry for Germany (NCRR-G):** District-year registry containing administrative information, predictor variables, predicted Regional Climate Risk Scores (RCRS), and assigned climate risk classes.

- **Germany Climate Risk Map:** National NUTS-3 choropleth map displaying the median predicted Regional Climate Risk Score (1990–2025) for all modelled districts.

- **Saved model and preprocessing artefacts:** Trained FFNN model, preprocessing pipeline, feature scaler, model configuration, SHAP artefacts and deployment metadata

## Reproducibility

- **Python version:** 3.12

- **Environment file:** requirements.txt

- **Main notebooks/scripts:** Notebooks 00–09; Notebook 09 contains the complete modelling pipeline

- **Instructions for reproducing results:** Clone the repository, install dependencies from requirements.txt and execute the notebooks sequentially from Notebook 02 to Notebook 09.

- **Known limitations:** The modelling dataset contains 289 complete-case districts. Results represent current-climate conditions (1990–2025) and are intended for research and demonstration purposes.

## Ethics and Governance

- **Intended use:** Climate risk assessment, research, education and decision support.

- **Prohibited or inappropriate use:** Not intended as the sole basis for financial, regulatory or emergency management decisions.

- **Bias and coverage limitations:** Model performance depends on available climate and socioeconomic data and may not capture all local risk drivers.

- **Human oversight:** Model outputs should always be interpreted alongside expert judgement.

- **AI assistance disclosure:** Parts of the software development, documentation and project preparation were developed with assistance from OpenAI ChatGPT under human supervision. Final design decisions, implementation, validation and interpretation were performed by the project author.