# Estimating Nonlinear Insulin-Glucose Dynamics in Critically-ill Patients.

This projects contains the source code for my Master's thesis. The main
objectives of the project was to develop pipeline for generating synthetic
patient trajectories, investigating the observability of the ICING model,
compare different nonlinear estimators, and different parameter estimation
methods.

## Project Layout

```
thesis/
├── notebooks/
│   ├── 00_Patient_Cohort.ipynb
│   ├── 01_Observability_Analysis.ipynb
│   ├── 02_Integral_Estimation.ipynb
│   ├── 03_Estimator_Comparison.ipynb
│   ├── 04_Parameter_Estimation.ipynb
│   ├── 05_Parameter_Estimation.ipynb
│   └── plt_config.py
├── scripts/
│   ├── 00_Parameter_Distributions.py
│   ├── 00_Patient_Cohort.py
│   ├── 01_Observability_Analysis.py
│   ├── 02_Integral_Estimation.py
│   ├── 03_Estimator_Comparison.py
│   ├── 04_Cancer_Err.py
│   ├── 04_Parameter_estimation_augment_vary.py
│   ├── 04_Parameter_estimation_augment.py
│   ├── 04_Parameter_estimation_integral_vary.py
│   └── 04_Parameter_estimation_integral.py
├── src/
│   └── thesis/
│       ├── _ _init _ _.py
│       ├── edges_00.npy
│       ├── ext_kalman_filter.py
│       ├── feeding_histogram.npz
│       ├── gramian_obs.py
│       ├── heights_00.npy
│       ├── icing_model.py
│       ├── icing_true.py
│       ├── insulin_histogram.npz
│       ├── param_est.py
│       ├── particle_filter.py
│       ├── patient_cohort.py
│       └── utils.py
├── .gitignore
├── .python-version
├── config.toml
├── pyproject.toml
├── README.md
└── uv.lock
```

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then clone the repository and install the project dependencies:

```bash
git clone https://github.com/jumulv/Estimating-Insulin-Glucose-Dynamics.git
cd thesis
uv sync
```

## Run

To run one of the scripts, use the `uv run` command:

```bash
uv run 00_Patient_Cohort.py
```
