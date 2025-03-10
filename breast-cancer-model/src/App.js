import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ModelSelection from "./components/ModelSelection";
import SVMPage from "./components/SVMPage";
import RFPage from "./components/RFPage";
import LRPage from "./components/LRPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ModelSelection />} />
        <Route path="/svm" element={<SVMPage />} />
        <Route path="/random-forest" element={<RFPage />} />
        <Route path="/logistic-regression" element={<LRPage />} />
      </Routes>
    </Router>
  );
}

export default App;
