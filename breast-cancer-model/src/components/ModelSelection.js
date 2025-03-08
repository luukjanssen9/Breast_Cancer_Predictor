import React from "react";
import { useNavigate } from "react-router-dom";

function ModelSelection() {
  const navigate = useNavigate();
  console.log("ModelSelection loaded");
  return (
    <div className="App">
      <h1>Select a Model</h1>
      <button onClick={() => navigate("/svm")}>SVM Model</button>
      <button onClick={() => navigate("/random-forest")}>Random Forest Model</button>
    </div>
  );
}

export default ModelSelection;
