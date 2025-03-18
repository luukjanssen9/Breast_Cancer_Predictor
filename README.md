# Breast Cancer Detection Model

## Project Overview
This project aims to build a machine learning model for breast cancer detection using the **Breast Cancer Wisconsin Diagnostic Dataset**. The model classifies tumors as benign or malignant based on input features extracted from cell nuclei.

## Dataset
We are using the [Breast Cancer Wisconsin Diagnostic Dataset](https://www.kaggle.com/datasets/utkarshx27/breast-cancer-wisconsin-diagnostic-dataset). This dataset contains features computed from digitized images of fine needle aspirate (FNA) biopsies of breast mass tissues.

## Model
This project includes four different machine learning models:
- **Support Vector Machine (SVM)**
- **Logistic Regression**
- **Random Forest**
- **Artificial Neural Network**

Each model has a corresponding script (`create_svm.py`, `create_logistic_regression.py`, `create_random_forest.py`) that can be run to train the model and generate the necessary `.pkl` files for the model and the feature scaler. The trained models are stored as pickle files (`backend/[model_name]_model.pkl`), and the scalers are stored as (`backend/[model_name]_scaler.pkl`) in the models folder, once the corresponding scripts have been run.
*ANN doesn't have webapp functionality yet, but the code can be found in (`backend/ann`)
## Setup Instructions

### 1. Create a Virtual Environment
#### On Linux/macOS:
```sh
python -m venv .venv
source .venv/bin/activate
```

#### On Windows (Command Prompt):
```sh
python -m venv .venv
.venv\Scripts\activate.bat
```

#### On Windows (PowerShell):
```sh
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Running the React Frontend
```sh
cd breast-cancer-model
npm install  # Run this once if not already installed
npm start
```

### 4. Running the Backend
```sh
cd backend
python3 app.py
```

## Usage
- The React frontend provides an interface for users to input cell feature values and get predictions.
- The backend serves API endpoints for model inference.

## Future Improvements
- Improve model performance with hyperparameter tuning.
- Implement additional classification models for comparison.
- Deploy the model as a cloud-based web service.


