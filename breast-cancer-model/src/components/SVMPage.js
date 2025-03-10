import React, { useState } from "react";
import { sendPrediction } from "../api/api.js"; // Helper function for requests
import "../styles/SVMPage.css"; // Import the updated CSS

function SVMPage() {
  const [formData, setFormData] = useState({
    radius_mean: "",
    texture_mean: "",
    perimeter_mean: "",
    area_mean: "",
    smoothness_mean: "",
    compactness_mean: "",
    concavity_mean: "",
    concave_points_mean: "",
    symmetry_mean: "",
    fractal_dim_mean: "",
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
    <div className="svm-container">
      <h2>Support Vector Machine Model</h2>
      <form onSubmit={handleSubmit} className="svm-form">
        {Object.keys(formData).map((key) => (
          <div key={key} className="form-group">
            <label>{key.replace(/_/g, " ")}:</label>
            <input
              type="number"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
              step="0.01"
            />
          </div>
        ))}
        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? "Processing..." : "Predict"}
        </button>
      </form>
      {error && <p className="error-message">Error: {error}</p>}
      {prediction !== null && (
        <p className={`result-message ${prediction === 1 ? "benign" : "malignant"}`}>
          Prediction: {prediction === 1 ? "Benign" : "Malignant"}
        </p>
      )}
    </div>
  );
}

export default SVMPage;
