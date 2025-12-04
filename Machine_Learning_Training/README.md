## Description

1_Intro_Data_Science.ipynb:  This notebook is the basics.  Pull data from Snowflake into a pandas dataframe, do some basic cleaning, train an xgboost model, deploy to the registry and call the model using SQL for batch inference.

2_Deploy_to_container:  More extensive cleaning, train more hyperparameters leveraging grid search, then deploy to a container.  This will allow us to create a service and perform real time model inference.

3_Call_Endpoint.py:  This shows how to call the model endpoint externally.  In this example we call it from out laptops.

4_Remote_ml_jobs.ipynb:  Leveraging a local IDE such as VSCode but leverage a snowflake compute pool for the model training and cleaning.

5_ML_OPS.ipynb:  Feature store, model registry with experiement tracking/observability/multinode training with Ray.

## Requirements

- Python >= 3.10, < 3.11
- See `pyproject.toml` for full list of dependencies

## Installation

```bash
# Install dependencies using uv
uv sync
```
