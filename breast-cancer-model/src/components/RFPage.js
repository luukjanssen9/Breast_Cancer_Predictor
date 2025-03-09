import React, { useState } from "react";
import { sendPrediction } from "../api/api.js";  // Helper function to send requests

function RFPage() {
  const [formData, setFormData] = useState({
    area_worst: "", concave_points_worst: "", radius_worst: "", perimeter_worst: "",
    concave_points_mean: ""
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
    <div className="App">
      <h2>RF Model</h2>
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

export default RFPage;
