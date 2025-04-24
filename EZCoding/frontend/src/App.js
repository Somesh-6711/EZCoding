import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [code, setCode] = useState("");
  const [filename, setFilename] = useState("");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const API = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

  // Simple dark-mode toggle
  useEffect(() => {
    document.body.style.background = darkMode ? "#1e1e2f" : "#f4f6fc";
    document.body.style.color = darkMode ? "#eee" : "#333";
  }, [darkMode]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      let resp;
      if (file) {
        const form = new FormData();
        form.append("file", file);
        resp = await axios.post(`${API}/explain_code`, form, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      } else {
        resp = await axios.post(`${API}/explain_code`, { code, filename });
      }
      setResult(resp.data);
    } catch (err) {
      console.error(err);
      alert("Error explaining code");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>CodeWise 🔍</h1>
      <div className="toggle-wrapper">
        <label>
          <input
            type="checkbox"
            checked={darkMode}
            onChange={() => setDarkMode((v) => !v)}
          />{" "}
          Dark Mode
        </label>
      </div>

      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Paste your code here..."
          value={code}
          onChange={(e) => setCode(e.target.value)}
          disabled={!!file}
          required={!file}
        />
        <input
          type="text"
          placeholder="filename.ext (optional)"
          value={filename}
          onChange={(e) => setFilename(e.target.value)}
          disabled={!!file}
        />
        <div>
          <label>
            or upload a file:
            <input
              type="file"
              onChange={(e) => {
                setFile(e.target.files[0]);
                setCode("");
                setFilename("");
                setResult(null);
              }}
            />
          </label>
          {file && (
            <button
              type="button"
              onClick={() => setFile(null)}
              className="button"
            >
              Clear File
            </button>
          )}
        </div>
        <button type="submit" disabled={loading} className="button">
          {loading ? "Explaining…" : "Explain Code"}
        </button>
      </form>

      <div className="result">
        {!result ? (
          <p>Your explanation will appear here…</p>
        ) : (
          <>
            <h2>Language: {result.language}</h2>
            <pre>{result.explanation}</pre>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
