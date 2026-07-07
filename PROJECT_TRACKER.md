# Climate & ESG Risk Intelligence Germany
## AI Engineering Project Tracker

**Project Status:** 🟡 Planning & Data Engineering

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

- [ ] Climate risk literature
- [ ] ESG literature
- [ ] Neural Networks literature
- [ ] Explainable AI literature
- [ ] German regulatory framework
- [ ] Final bibliography

---
# Phase 3 – Data Acquisition
- [x] Download datasets
- [x] Identify data sources
- [x] Additional datasets -NUTS-2 and NUTS-3


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


- Immediate Next Phase:
☐ Merge climate and socio-economic datasets
☐ Build Climate–ESG Master Dataset


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
☐ Harmonize socioeconomic datasets to Project400 (target_nuts3_id)
⬜ Merge climate and socioeconomic datasets
⬜ Create Climate-ESG Master Dataset
---

# Phase 6 – Feature Engineering

- [ ] Feature selection
- [ ] Scaling
- [ ] Encoding
- [ ] Target creation

---

# Phase 7 – AI Model

- [ ] Build FFNN
- [ ] Train model
- [ ] Hyperparameter tuning
- [ ] Model evaluation
- [ ] SHAP explainability

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

- [ ] README
- [ ] Data Catalog
- [ ] User Guide
- [ ] Technical Report

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
- [ ] Milestone 2b – Socioeconomic Harmonization Complete
- [ ] Milestone 3 – Master Dataset Ready
- [ ] Milestone 3 – Master Dataset Ready
- [ ] Milestone 4 – FFNN Complete
- [ ] Milestone 5 – Explainability
- [ ] Milestone 6 – API Live
- [ ] Milestone 7 – Frontend Live
- [ ] Milestone 8 – Project Complete