import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Set up paths
base_dir = Path(__file__).resolve().parent / "models"

# Load models
models = {
    "svm": pickle.load(open(base_dir / "svm_model.pkl", "rb")),
    "random_forest": pickle.load(open(base_dir / "rf_model.pkl", "rb"))
}

# Load scalers (each model has its own scaler)
scalers = {
    "svm": pickle.load(open(base_dir / "svm_scaler.pkl", "rb")),
    "random_forest": pickle.load(open(base_dir / "rf_scaler.pkl", "rb"))
}

# Define expected features for each model
# If features need to be changed it needs to be done here, in the js file and in the create_<mode> file
feature_sets = {
    "svm": [
        'x.radius_mean', 'x.texture_mean', 'x.perimeter_mean', 'x.area_mean',
        'x.smoothness_mean', 'x.compactness_mean', 'x.concavity_mean',
        'x.concave_points_mean', 'x.symmetry_mean', 'x.fractal_dim_mean'
    ],
    "random_forest": [
        'x.area_worst', 'x.concave_points_worst', 'x.radius_worst',
        'x.perimeter_worst', 'x.concave_points_mean'
    ]
}

@app.route('/predict/<model_name>', methods=['POST'])
def predict(model_name):
    if model_name not in models:
        return jsonify({'error': f'Model {model_name} not found'}), 400

    try:
        data = request.json
        input_df = pd.DataFrame([data])

        # Get model-specific features
        features = feature_sets[model_name]

        # Handle missing features (default to 0)
        for col in features:
            if col not in input_df.columns:
                print(f"Adding missing column: {col}")
                input_df[col] = 0

        # Ensure correct feature order
        input_df = input_df[features].astype(float)

        # Scale input data
        input_scaled = scalers[model_name].transform(input_df)

        # Make prediction
        prediction = models[model_name].predict(input_scaled)[0]
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/features/<model_name>', methods=['GET'])
def get_features(model_name):
    """Returns the expected features for a given model."""
    if model_name not in feature_sets:
        return jsonify({'error': f'Model {model_name} not found'}), 400
    return jsonify({'features': feature_sets[model_name]})

if __name__ == '__main__':
    app.run(debug=True)
