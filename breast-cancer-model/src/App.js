import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ModelSelection from "./components/ModelSelection";
import SVMPage from "./components/SVMPage";
import RFPage from "./components/RFPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ModelSelection />} />
        <Route path="/svm" element={<SVMPage />} />
        <Route path="/random-forest" element={<RFPage />} />
      </Routes>
    </Router>
  );
}

export default App;
