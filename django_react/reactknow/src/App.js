import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CreateQuestionForm from "./CreateQuestionForm";
import Home from "./Home"; // Ensure correct import path
import "./styles.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add_question" element={<CreateQuestionForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
