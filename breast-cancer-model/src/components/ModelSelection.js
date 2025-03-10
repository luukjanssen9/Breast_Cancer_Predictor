import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/ModelSelection.css";

function ModelSelection() {
  const navigate = useNavigate();

  return (
    <div className="model-selection">
      <h1>Breast Cancer Predictor</h1>
      <div className="models">
        <button className="model-btn" onClick={() => navigate("/svm")}>
          SVM Model
        </button>
        <button className="model-btn" onClick={() => navigate("/random-forest")}>
          Random Forest Model
        </button>
      </div>
    </div>
  );
}

export default ModelSelection;
