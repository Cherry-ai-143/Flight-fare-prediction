# Flight Fare Prediction

- LinkedIn [Mohan c c](https://github.com/Cherry-ai-143/)

## About The Project

Welcome to the Flight Fare Prediction App! This project aims to provide users with a tool to predict flight fares based on various parameters, allowing them to make informed decisions when booking air travel. The app utilizes machine learning algorithms trained on historical flight data to estimate future fares. Users can input details such as departure and arrival locations, date, and airline preferences to receive an estimated fare for their desired flight. Whether you're a frequent traveller or planning your next vacation, this app is designed to make the flight booking process more transparent and efficient. Feel free to explore, contribute, and enhance the functionality of this Flight Fare Prediction App!

## Built With

 - Pandas
 - Numpy
 - Scikit-learn
 - Seaborn
 - Matplotlib
# Flight Fare Prediction

This repository implements a Flask web app that predicts flight fares using scikit-learn models. It includes a training pipeline that produces preprocessing and model artifacts in the `Artifacts/` folder.

## Quick summary
- Web API/UI: `app.py` with templates in `templates/`
- Training pipeline: `train.py` which runs the pipeline in `src/FlightPricePrediction/pipeline/` and creates artifacts under `Artifacts/`
- Data generator: `create_sample_data.py` (synthetic data for demo/training)

## Tech stack
- Python 3.10
- Flask
- pandas, numpy
- scikit-learn
- mlflow (optional logging)
- dvc (optional data versioning)

## Run locally (PowerShell)
1. Open PowerShell and go to the project root:

```powershell
cd C:\Users\91734\Flight-Fare-Prediction
```

2. Activate virtualenv:

```powershell
.\venv\Scripts\Activate.ps1
```

3. (Optional) Install dependencies:

```powershell
pip install -r requirements.txt
```

4. (Optional) Generate demo data:

```powershell
python create_sample_data.py
```

5. Train the model (creates `Artifacts/`):

```powershell
python train.py
```

6. Run the webapp:

```powershell
python app.py
```

7. Open the UI in a browser:

http://localhost:5000

## Run (cmd.exe)
```cmd
cd C:\Users\91734\Flight-Fare-Prediction
venv\Scripts\activate.bat
pip install -r requirements.txt
python create_sample_data.py
python train.py
python app.py
```

## Important files
- `app.py` — Flask server and endpoints
- `templates/form.html`, `templates/result.html` — UI templates
- `train.py` — entry to run training pipeline
- `src/FlightPricePrediction/components/` — ingestion, transformation, trainer, evaluation
- `src/FlightPricePrediction/pipeline/` — training and prediction pipelines
- `Artifacts/` — `Preprocessor.pkl`, `Model.pkl`, CSVs created by training

## Troubleshooting
- No page at `http://localhost:5000`:
   - Confirm `python app.py` is running in the terminal (Ctrl+C to stop and restart).
   - Check port usage: `netstat -ano | findstr :5000`.
   - Allow Python in Windows Firewall if blocked.

- Missing artifacts error (`Preprocessor.pkl` or `Model.pkl` not found):
   - Run `python train.py` to create artifacts.
   - Confirm files exist under `Artifacts/`.

- MLflow `PermissionError` during training:
   - MLflow may try to write to a protected path. Set a local tracking URI:

```python
import mlflow, os
mlflow.set_tracking_uri('file://' + os.path.abspath('mlruns'))
```

or set environment variable in PowerShell before training:

```powershell
$env:MLFLOW_TRACKING_URI = "file://%CD%\\mlruns"
```

- `dvc pull` fails / no remote configured:
   - This repo contains a `dvc.yaml` stage but no DVC remote is configured. Either configure a remote or run the training pipeline locally to generate artifacts.

## Model & pipeline notes
- Preprocessing: `ColumnTransformer` combining numeric (`SimpleImputer` + `MinMaxScaler`) and categorical (`SimpleImputer` + `OrdinalEncoder` + `MinMaxScaler`) pipelines.
- Candidate models: `LinearRegression`, `Lasso`, `Ridge`, `ElasticNet`, `DecisionTreeRegressor`, `RandomForestRegressor`.
- Selection criterion: best R² on test set; the best model is saved to `Artifacts/Model.pkl`.

## Next steps (suggested)
- Configure MLflow tracking to avoid permission errors.
- Configure DVC remote if using remote data.
- Add unit tests for `PredictPipeline` and `CustomData`.
- For production, run behind a WSGI server and disable Flask debug mode.

---
If you want, I can also add a short troubleshooting script or automatically set `mlflow.set_tracking_uri()` inside the training pipeline. Which would you prefer?
