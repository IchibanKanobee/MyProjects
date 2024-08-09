import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css"; // Import your CSS file

const ShowQuestionForm = () => {
  const [subjects, setSubjects] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/subjects/")
      .then((response) => setSubjects(response.data))
      .catch((error) => console.error("Error fetching subjects:", error));
  }, []);

  useEffect(() => {
    if (selectedSubject) {
      axios
        .get(
          `http://localhost:8000/api/questions/?subject_id=${selectedSubject}&page=${currentPage}`
        )
        .then((response) => {
          setQuestions(response.data.questions);
          setTotalPages(response.data.total_pages);
          setCurrentPage(response.data.page);
        })
        .catch((error) => console.error("Error fetching questions:", error));
    }
  }, [selectedSubject, currentPage]);

  const handleSubjectChange = (e) => {
    setSelectedSubject(e.target.value);
    setCurrentPage(1); // Reset to first page whenever subject changes
  };

  const handlePageChange = (newPage) => {
    if (newPage > 0 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
  };

  return (
    <div className="container">
      <h1>Questions</h1>
      <div>
        <label htmlFor="subject-select">Select Subject: </label>
        <select
          id="subject-select"
          onChange={handleSubjectChange}
          className="form-control"
        >
          <option value="">--Choose a Subject--</option>
          {subjects.map((subject) => (
            <option key={subject.subject_id} value={subject.subject_id}>
              {subject.name}
            </option>
          ))}
        </select>
      </div>
      <div>
        {questions.map((question, index) => (
          <div key={question.question_id}>
            <h2>Question {index + 1}</h2>
            <p>{question.question_text}</p>
            {question.image && (
              <img
                src={`http://localhost:8000/media/${question.image}`}
                alt="Question related"
                className="img-fluid"
              />
            )}
            {question.video && (
              <video
                src={`http://localhost:8000/media/${question.video}`}
                controls
                className="img-fluid"
              />
            )}
            <p>
              <strong>Answer:</strong> {question.answer_text}
            </p>
          </div>
        ))}
      </div>
      <div>
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className="btn btn-primary"
        >
          Previous
        </button>
        <span>
          {" "}
          Page {currentPage} of {totalPages}{" "}
        </span>
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className="btn btn-primary"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ShowQuestionForm;
