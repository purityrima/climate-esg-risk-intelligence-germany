# Climate & ESG Risk Intelligence Germany
## AI Engineering Project Tracker

**Project Status:** 🟢 AI Engineering Completed | 🟡 Documentation & Final Submission in Progress

---

# Phase 1 – Project Foundation

- [x] Define project scope
- [x] Select study area (Germany, NUTS-3)
- [x] Identify target sectors
- [x] Design repository structure
- [x] Create GitHub repository
- [x] Clone repository locally
- [x] Configure Git connection
- [x] Create project documentation

---

# Phase 2 – Literature Review

- [x] Climate risk literature
- [x] ESG literature
- [x] Neural Networks literature
- [x] Explainable AI literature
- [x] German regulatory framework
- [x] Final bibliography

---
# Phase 3 – Data Acquisition
- [x] Download datasets
- [x] Identify data sources
- [x] Additional datasets -NUTS-2 and NUTS-3
- [x] Assess variables and metadata
- [x] Create Dataset Assessment Table


# Phase 4 – Dataset Exploration & Selection

### Climate datasets

- [x] Explore Heat dataset (.nc)
- [x] Explore Flood dataset (.nc)
- [x] Explore Drought dataset (.nc)
- [x] Validate NUTS-2 → NUTS-3 Spatial Crosswalk (401 districts)

| Notebook                                            | Status     | Output                                         | Notes                                   |
| --------------------------------------------------- | ---------- | ---------------------------------------------- | --------------------------------------- |
| 01 Climate Dataset Inventory                        | ✅ Complete | Inventory                                      | Initial climate dataset review          |
| 02 Flood Proxy (Rx5day)                             | ✅ Complete | `rx5day_germany_nuts2_1990_2025.nc`            | Germany subset extracted and documented |
| 03 Drought Proxy (Meteorological Drought Magnitude) | ✅ Complete | `drought_magnitude_germany_nuts2_1990_2025.nc` | Germany subset extracted and documented |
| 04 Heat Proxy (Climatological Heatwave Days)        | ✅ Complete | `heatwave_days_germany_nuts2_1990_2025.nc`     | Germany subset extracted and documented |


| Notebook | Status | Progress | Notes |
|---|---|---:|---|
| `08_crosswalks_and_dataset_harmonization.ipynb` | ✅ Completed | 100% | Administrative crosswalk validated; climate datasets harmonized to 400 districts; socioeconomic datasets prepared for 1990–2025; integrated master dataset created with **14,400 observations** and exported to `data/processed/master/`. Crosswalk refinement remains optional future work and does not block model development. |




### Current Project Progress

✔ Climate hazard datasets explored and documented:
- Flood (Rx5day)
- Drought Magnitude
- Heatwave Days

✔ NUTS-2 → NUTS-3 Spatial Crosswalk constructed

✔ Spatial compatibility with INKAR validated

✔ 401 vs. 400 district discrepancy resolved

### Completed

☑ Build administrative crosswalk (Project400)
☑ Build spatial crosswalk (NUTS-2 → Project400)
☑ Harmonize climate datasets
    ☑ Heatwave
    ☑ Flood (Rx5day)
    ☑ Drought
☑ Merge climate and socio-economic datasets
☑ Build Climate–ESG Master Dataset

- Immediate Next Phase:
Project documentation, metadata preparation and final report.

### Socioeconomic datasets

- [X] Explore Population dataset
- [x] Explore GDP dataset
- [ ] Explore Infrastructure dataset
- [ ] Explore Land Use dataset

### Vulnerability datasets
- [x] Unemployment rate
- [ ] Adaptive Capacity Proxy

### Banking & Financial datasets

- [ ] Explore Banking Exposure dataset
- [ ] Explore ESG Indicator dataset

### Dataset assessment

- [ ] Assess variables and metadata
- [X] Assess temporal coverage
- [X] Assess spatial resolution
- [X] Assess missing values
- [X] Compare candidate datasets
- [ ] Create Dataset Assessment Table
- [X] Select datasets for the master dataset


# Phase 5 – Data Engineering
☑ Standardize CRS
☑ Build administrative crosswalk (Project400)
☑ Build spatial crosswalk (NUTS-2 → Project400)
☑ Validate spatial crosswalk
☑ Harmonize Germany climate datasets (1990–2025)
    ☑ Heatwave
    ☑ Flood (Rx5day)
    ☑ Drought

☑ Climate Harmonization Framework Complete
☑ Prepare and impute socioeconomic datasets
    - [x] GDP per capita
    - [x] Unemployment
    - [x] Population excluded due to incomplete district-level coverage
- [x] Harmonize socioeconomic datasets to Project400 (`target_nuts3_id`)
    - [x] GDP per capita
    - [x] Unemployment
- [x] Merge climate and socioeconomic datasets
- [x] Create Climate-ESG Master Dataset
---

# Phase 6 – Feature Engineering

- [x] Create complete-case modelling dataset (289 districts)
- [x] Exploratory data analysis
- [x] Distribution analysis
- [x] Correlation analysis
- [x] Pairwise relationship analysis
- [x] Outlier assessment
- [x] Temporal trend analysis
- [x] Statistical interpretation
- [x] Define preprocessing strategy based on EDA
- [x] Construct Regional Climate Risk Score
- [x] Evaluate log(x+1) transformation
- [x] Apply feature transformations
- [x] Train / Validation / Test split
- [x] Feature scaling

**Notes:** 
400 harmonized districts retained as the reference master dataset.
289 districts used for FFNN modelling after complete-case filtering to ensure no missing predictor values.
---

# Phase 7 – AI Model

- [x] Build Feed-Forward Neural Network
- [x] Train model
- [x] Hyperparameter tuning
- [x] Evaluate regression performance
- [x] Generate SHAP explanations
- [x] Generate Regional Risk Classes
- [x] Save trained FFNN model
- [x] Save preprocessing pipeline
- [x] Save deployment artifacts
- [x] Save SHAP artifacts
- [x] Build National Climate Risk Registry (NCRR-G)
- [x] Rank all modelled districts nationally
- [x] Generate Germany Climate Risk Map


---

# Phase 8 – API

- [ ] Flask backend
- [ ] REST endpoints
- [ ] Prediction endpoint
- [ ] Error handling

---

# Phase 9 – Frontend

- [ ] Dashboard
- [ ] Region selection
- [ ] Risk visualization
- [ ] Prediction interface

---

# Phase 10 – Testing

- [ ] Unit tests
- [ ] Integration tests
- [ ] API testing

---

# Phase 11 – Documentation

- [x] README
- [x] Data Catalog
- [x] Metadata
- [x] Literature
- [x] Technical Report

---

# Phase 12 – Deployment

- [ ] GitHub complete
- [ ] Heroku backend
- [ ] Vercel frontend
- [ ] Final presentation

---

## Milestones

- [x] Milestone 1 – Repository & Project Setup
- [x] Milestone 2a – Climate Harmonization Complete
- [x] Milestone 2b – Socioeconomic Harmonization Complete
  [x] Climate datasets harmonized to project district framework
  [x] GDP harmonized and imputed (1990–2025)
  [x] Unemployment harmonized and imputed (1990–2025)
  [x] Administrative crosswalk developed and validated
  [x] Integrated master dataset created
  [x] Master dataset exported to data/processed/master/
- [x] Milestone 3 - Master Dataset Ready
- [x] Milestone 4 - Exploratory Data Analysis Complete
- [x] Milestone 5 - Feature Engineering Complete
- [x] Milestone 6 - FFNN Complete
- [x] Milestone 7 - SHAP Explainability
- [x] National Climate Risk Registry (NCRR-G) generated
- [x] Germany Climate Risk Map generated
- [x] Model deployment artifacts exported
- [x] Milestone 8 – Repository Documentation Complete

- [ ] Milestone 9 - API Live
- [ ] Milestone 10 - Frontend Live
- [ ] Milestone 11 - Final Documentation & Project Submission


### Summary of Work Completed

- Climate and socioeconomic datasets successfully harmonized and integrated into the complete modelling dataset.
- Complete-case modelling dataset (289 districts × 36 years = 10,404 observations) prepared.
- Regional Climate Risk Score (RCRS) developed using a Feed-Forward Neural Network.
- Model trained, validated and evaluated successfully.
- SHAP explainability completed (global feature importance and local prediction explanation).
- National Climate Risk Registry for Germany (NCRR-G) generated.
- Germany Climate Risk Map generated.
- Model deployment artifacts exported and ready for API Deployment.
- Repository documentation prepared for reproducible project delivery.

### Latest Update (17 July 2026)

- Final FFNN pipeline completed successfully.
- Notebook 09 executes successfully from start to finish.
- SHAP explainability completed (global and local).
- National Climate Risk Registry for Germany (NCRR-G) generated.
- Germany Climate Risk Map generated.
- Deployment-ready model artefacts exported.
- Repository documentation completed (README, Metadata, Data Catalog, Literature).
- Final project report in progress.