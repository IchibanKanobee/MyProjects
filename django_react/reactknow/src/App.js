import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CreateQuestionForm from "./CreateQuestionForm";
import CreateSubjectForm from "./CreateSubjectForm";
import ShowQuestionForm from "./ShowQuestionForm"; // Adjust the path as needed
import Home from "./Home"; // Ensure correct import path
import "./styles.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add-question/" element={<CreateQuestionForm />} />
          <Route path="/add-subject/" element={<CreateSubjectForm />} />
          <Route path="/questions/" element={<ShowQuestionForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
