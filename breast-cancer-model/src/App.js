import React, { useState } from "react";
import "./App.css";

function App() {
  // Form Input Values
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

  // Prediction Results
  const [prediction, setPrediction] = useState(null);
  // Loading State
  const [loading, setLoading] = useState(false);
  // Error state
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      // update field
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // Format data to match backend expectations
      const formattedData = {};
      Object.keys(formData).forEach((key) => {
        formattedData[`x.${key}`] = parseFloat(formData[key]) || 0;
      });

      console.log("Sending Data:", formattedData); // Debugging step

      // Send data to Flask backend
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formattedData),
      });

      console.log("Response Status:", response.status); // Debugging step

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Failed to get prediction");
      }

      const result = await response.json();
      console.log("Received Result:", result); // Debugging step
      setPrediction(result.prediction);
    } catch (err) {
      console.error("Error:", err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const renderResult = () => {
    if (loading) return <p>Processing...</p>;
    if (error) return <p className="error">Error: {error}</p>;
    if (prediction !== null) {
      return (
        <div className="prediction-result">
          <h3>Prediction Result</h3>
          <p className={prediction === 1 ? "benign" : "malignant"}>
            {prediction === 1 ? "Benign (Non-Cancerous)" : "Malignant (Cancerous)"}
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="App">
      <header className="App-header">Breast Cancer Detection</header>
      <div className="App-body">
        <p className="body-header">Tumor Features</p>
        <form onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <label key={key}>
              {key.replace("_", " ")}:
              <input
                type="number"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                required
                step="0.01"
              />
            </label>
          ))}
          <button type="submit" disabled={loading}>
            {loading ? "Processing..." : "Predict"}
          </button>
        </form>
        {renderResult()}
      </div>
    </div>
  );
}

export default App;
