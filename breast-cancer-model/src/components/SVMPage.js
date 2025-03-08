import React, { useState } from "react";
import { sendPrediction } from "../api/api.js";  // Helper function to send requests

function SVMPage() {
  const [formData, setFormData] = useState({
    radius_mean: "", texture_mean: "", perimeter_mean: "", area_mean: "",
    smoothness_mean: "", compactness_mean: "", concavity_mean: "",
    concave_points_mean: "", symmetry_mean: "", fractal_dim_mean: ""
  });
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const result = await sendPrediction(formData, "svm");
      setPrediction(result.prediction);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h2>SVM Model</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <label key={key}>
            {key.replace("_", " ")}:
            <input type="number" name={key} value={formData[key]} onChange={handleChange} required step="0.01" />
          </label>
        ))}
        <button type="submit" disabled={loading}>{loading ? "Processing..." : "Predict"}</button>
      </form>
      {error && <p className="error">Error: {error}</p>}
      {prediction !== null && <p className="result">Prediction: {prediction === 1 ? "Benign" : "Malignant"}</p>}
    </div>
  );
}

export default SVMPage;
