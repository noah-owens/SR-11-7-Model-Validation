# SR 11-7 Model Validation Portfolio

[![Docstring Lint](https://github.com/noah-owens/SR-11-7-Model-Validation/actions/workflows/docstring-lint.yaml/badge.svg)](https://github.com/noah-owens/SR-11-7-Model-Validation/actions/workflows/docstring-lint.yaml)

This project demonstrates how to validate a predictive model against the Federal Reserve’s SR 11-7 guidance. It intends to simulate a full model lifecycle — from documentation -> data integrity -> performance testing -> governance — using the publicly available LendingClub Loans dataset.

## Overview

- **Model Type**: Logistic regression for loan default prediction
- **Dataset**: LendingClub accepted and rejected loan applications (2007–2018)
- **Validation Framework**: SR 11-7 Model Risk Management
- **Format**: Executable Python notebooks with embedded commentary and visual diagnostics

| Notebook | Purpose |
|---------|---------|
| `01_model_overview.ipynb` | Define model purpose, assumptions, and business context |
| `02_data_quality.ipynb` | Assess input data integrity, completeness, and relevance |
| `03_model_validation.ipynb` | Perform backtesting, sensitivity analysis, benchmarking |
| `04_documentation.ipynb` | Generate SIPOC diagrams, model lineage, and audit trails |
| `05_governance_checks.ipynb` | Simulate override logs, usage flags, and approval workflows |

## Libraries

- `pandas`, `numpy`, `matplotlib`, `seaborn` — data wrangling and visualization
- `scikit-learn` — modeling and metrics
- `shap`, `lime` — explainability
- `graphviz`, `diagrams` — SIPOC and flowcharts
- `python-dotenv` — environment variable management
- `pydocstyle` — docstring linting

## Linting & Documentation Standards

This project uses [`pydocstyle`](https://www.pydocstyle.org/) to enforce Google-style docstrings across all modules.

### Linting Rules
- All public functions must include:
  - Argument descriptions
  - Return types
  - Raised exceptions (if applicable)
- Docstrings follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
