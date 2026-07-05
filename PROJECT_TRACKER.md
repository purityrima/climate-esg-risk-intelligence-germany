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
- [x] Additional datasets


# Phase 4 – Dataset Exploration & Selection

### Climate datasets

- [x] Explore Heat dataset (.nc)
- [x] Explore Flood dataset (.nc)
- [x] Explore Drought dataset (.nc)

| Notebook                                            | Status     | Output                                         | Notes                                   |
| --------------------------------------------------- | ---------- | ---------------------------------------------- | --------------------------------------- |
| 01 Climate Dataset Inventory                        | ✅ Complete | Inventory                                      | Initial climate dataset review          |
| 02 Flood Proxy (Rx5day)                             | ✅ Complete | `rx5day_germany_nuts2_1990_2025.nc`            | Germany subset extracted and documented |
| 03 Drought Proxy (Meteorological Drought Magnitude) | ✅ Complete | `drought_magnitude_germany_nuts2_1990_2025.nc` | Germany subset extracted and documented |
| 04 Heat Proxy (Climatological Heatwave Days)        | ✅ Complete | `heatwave_days_germany_nuts2_1990_2025.nc`     | Germany subset extracted and documented |

Current Project Progress

✅ Climate hazard datasets completed:
• Flood (Rx5day)
• Drought Magnitude
• Heatwave Days

Next phase:
• Exposure datasets
    □ Population Density
    □ GDP per Capita

• Vulnerability datasets
    □ Urbanization Proxy
    □ Adaptive Capacity Proxy

• Master Dataset Construction
    □ Merge climate, exposure, and vulnerability datasetsa



### Socioeconomic datasets

- [X] Explore Population dataset
- [x] Explore GDP dataset
- [ ] Explore Infrastructure dataset
- [ ] Explore Land Use dataset

### Vulnerability datasets
- [ ] Unemployment
- [ ] Adaptive Capacity Proxy

### Banking & Financial datasets

- [ ] Explore Banking Exposure dataset
- [ ] Explore ESG Indicator dataset

### Dataset assessment

- [ ] Assess variables and metadata
- [ ] Assess temporal coverage
- [ ] Assess spatial resolution
- [ ] Assess missing values
- [ ] Compare candidate datasets
- [ ] Create Dataset Assessment Table
- [ ] Select datasets for the master dataset


# Phase 5 – Data Engineering
- [ ] Standardize CRS
- [ ] Clean datasets
- [ ] Aggregate to NUTS-3
- [ ] Merge datasets
- [ ] Create master dataset

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
- [ ] Milestone 2 – Data Engineering Complete
- [ ] Milestone 3 – Master Dataset Ready
- [ ] Milestone 4 – FFNN Complete
- [ ] Milestone 5 – Explainability
- [ ] Milestone 6 – API Live
- [ ] Milestone 7 – Frontend Live
- [ ] Milestone 8 – Project Complete