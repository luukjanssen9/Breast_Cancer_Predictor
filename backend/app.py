import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
import pickle
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the backend directory dynamically
base_dir = Path(__file__).resolve().parent  # Assuming app.py is inside backend/
model_path = base_dir / "svm_model.pkl"
scaler_path = base_dir / "scaler.pkl"

print(f"Model Path: {model_path}")
print(f"Scaler Path: {scaler_path}")

# Load the model and scaler if they exist
if model_path.exists() and scaler_path.exists():
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    print("✅ Model and Scaler loaded successfully.")
else:
    print("❌ Model files not found. Please train and save the model first.")
    exit(1)  # Exit if model files are missing

# Define expected features (MATCHES TRAINING DATA)
features = [
    'x.radius_mean', 'x.texture_mean', 'x.perimeter_mean', 'x.area_mean',
    'x.smoothness_mean', 'x.compactness_mean', 'x.concavity_mean',
    'x.concave_points_mean', 'x.symmetry_mean', 'x.fractal_dim_mean'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Convert input JSON into a DataFrame
        input_df = pd.DataFrame([data])

        # Rename columns to match training feature names
        input_df = input_df.rename(columns={col: f"x.{col}" for col in input_df.columns})

        # Handle missing features (default to 0)
        for col in features:
            if col not in input_df.columns:
                input_df[col] = 0

        # Ensure correct feature order
        input_df = input_df[features]

        # Convert to float (ensures numerical format)
        input_df = input_df.astype(float)

        # Scale input data
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(input_scaled)[0]

        # Return JSON response
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
