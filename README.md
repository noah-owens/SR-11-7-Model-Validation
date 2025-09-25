# SR 11-7 Model Validation Portfolio

[![Docstring Lint](https://github.com/noah-owens/SR-11-7-Model-Validation/actions/workflows/docstring-lint.yaml/badge.svg)](https://github.com/noah-owens/SR-11-7-Model-Validation/actions/workflows/docstring-lint.yaml)

This project demonstrates how to validate a predictive model against the Federal Reserve’s SR 11-7 guidance. It intends to simulate a full model lifecycle — from documentation -> data integrity -> performance testing -> governance — using the publicly available LendingClub Loans dataset.

## Usage

At least for now, fetching the dataset is not automated. If you would like to follow along and use the program interactively, clone the repository and provide your own copies of `accepted_2007_to_2018Q4.csv` & `rejected_2007_to_2018Q4.csv` from this page on [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

Save the csv files into `data/`. If you chose to save them in a different location, you will need to modify the filepaths in `config.py`.

## Overview

- **Model Type**: Logistic regression - loan default prediction
- **Dataset**: LendingClub accepted and rejected loan applications (2007–2018)

| Notebook | Purpose |
|---------|---------|
| `01_DataOverview.ipynb` | Define model purpose, expose top level summary of dataset |
| `02_DataQuality.ipynb` | Quantify missingness, cardinality, data quality issues |

## Libraries

- `fastparquet` - caching data
- `pandas`, `numpy`, `matplotlib`, `seaborn` — data wrangling and visualization
- `scikit-learn` — modeling and metrics
- `shap`, `lime` — explainability
- `graphviz`, `diagrams` — SIPOC and flowcharts
- `pydocstyle` — docstring linting

## Linting & Documentation Standards

### Linting Rules
- All public functions must include:
  - Argument descriptions
  - Return types
  - Raised exceptions (if any)
- Docstrings follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)