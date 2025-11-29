# Automated Data Pipeline & Validation

## Overview
This project demonstrates a robust "Data DevOps" workflow. It simulates a Continuous Integration (CI) pipeline that generates synthetic data, performs statistical modeling to recover signal from noise, and automatically runs regression tests to validate the model's accuracy.

## Key Features
- **Synthetic Data Generation:** Generates linear datasets with injected Gaussian noise to simulate real-world data.
- **Statistical Fitting:** Uses linear regression to recover the original slope and intercept from the noisy data.
- **Automated QA:** Utilizes `pytest` to automatically verify that the fitted model falls within acceptable tolerance levels.

## Files
- `syntheticdata.py`: Script to generate the noisy dataset (`synthetic_data.csv`).
- `fitsyntheticdata.py`: Script to read the data, fit the model, and generate the visualization (`line_fit_plot.png`).
- `testfitsyntheticdata.py`: The automated test suite used to validate data integrity and model performance.

## Usage
Run the full pipeline steps:

1. Generate the data:
```bash
python syntheticdata.py

2. Fit the model and plot:
code
Bash
python fitsyntheticdata.py

3. Run the automated tests:
code
Bash
pytest