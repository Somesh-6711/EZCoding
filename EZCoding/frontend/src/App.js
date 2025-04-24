import React, { useState } from "react";
import axios from "axios";

function App() {
  const [code, setCode] = useState("");
  const [filename, setFilename] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const resp = await axios.post(
        `${process.env.REACT_APP_API_URL}/explain_code`,
        { code, filename }
      );
      setResult(resp.data);
    } catch (err) {
      console.error(err);
      alert("Error fetching explanation");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 800, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>CodeWise: Code Explainer</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={12}
          style={{ width: "100%", padding: "0.5rem", fontFamily: "monospace" }}
          placeholder="Paste your code here..."
          value={code}
          onChange={(e) => setCode(e.target.value)}
          required
        />
        <input
          type="text"
          style={{ width: "100%", padding: "0.5rem", marginTop: "1rem" }}
          placeholder="filename.ext (optional)"
          value={filename}
          onChange={(e) => setFilename(e.target.value)}
        />
        <button
          type="submit"
          disabled={loading}
          style={{
            marginTop: "1rem",
            padding: "0.75rem 1.5rem",
            background: "#0070f3",
            color: "white",
            border: "none",
            cursor: "pointer",
          }}
        >
          {loading ? "Explaining…" : "Explain Code"}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h2>Language: {result.language}</h2>
          <pre
            style={{
              background: "#f4f4f4",
              padding: "1rem",
              borderRadius: "4px",
              whiteSpace: "pre-wrap",
            }}
          >
            {result.explanation}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;
