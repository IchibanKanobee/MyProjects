import React, { useState } from "react";
import axios from "axios";
import "./styles.css"; // Import the custom CSS file

function CreateQuestionForm() {
  const [text, setText] = useState("");
  const [subject, setSubject] = useState("");
  const [correctAnswer, setCorrectAnswer] = useState("");
  const [image, setImage] = useState(null);
  const [video, setVideo] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("text", text);
    formData.append("subject", subject);
    formData.append("correct_answer", correctAnswer);
    if (image) {
      formData.append("image", image);
    }
    if (video) {
      formData.append("video", video);
    }

    try {
      const response = await axios.post(
        "http://djangoreactproj:8000/api/add-question/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log("Question added successfully:", response.data);
    } catch (error) {
      console.error("There was an error adding the question:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-5">
      <div className="form-group">
        <label htmlFor="subject">Subject:</label>
        <input
          type="text"
          className="form-control"
          id="subject"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="text">Question:</label>
        <textarea
          className="form-control large-textarea"
          id="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="correctAnswer">Answer:</label>
        <textarea
          className="form-control large-textarea"
          id="correctAnswer"
          value={correctAnswer}
          onChange={(e) => setCorrectAnswer(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="image">Image:</label>
        <input
          type="file"
          className="form-control-file"
          id="image"
          onChange={(e) => setImage(e.target.files[0])}
          accept="image/*"
        />
      </div>
      <div className="form-group">
        <label htmlFor="video">Video:</label>
        <input
          type="file"
          className="form-control-file"
          id="video"
          onChange={(e) => setVideo(e.target.files[0])}
          accept="video/*"
        />
      </div>
      <button type="submit" className="btn btn-primary mt-3">
        Add Question
      </button>
    </form>
  );
}

export default CreateQuestionForm;
