import React, { useState } from "react";
import { sendPrediction } from "../api/api.js"; // Helper function for requests
import "../styles/RFPage.css"; // Import the updated CSS

function RFPage() {
  const [formData, setFormData] = useState({
    area_worst: "",
    concave_points_worst: "",
    radius_worst: "",
    perimeter_worst: "",
    concave_points_mean: "",
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
      const result = await sendPrediction(formData, "random_forest");
      setPrediction(result.prediction);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rf-container">
      <h2>Random Forest Model</h2>
      <form onSubmit={handleSubmit} className="rf-form">
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

export default RFPage;
