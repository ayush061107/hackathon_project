import { useState } from "react";

function CreateDecision() {
  const [title, setTitle] = useState("");
  const [options, setOptions] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    alert(
      `Decision Created!\n\nTitle: ${title}\nOptions: ${options}`
    );
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Create Decision</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Decision Title</label>
          <br />
          <input
           type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Which phone should I buy?"
            style={{ width: "300px" }}
          />
        </div>

        <br />

        <div>
          <label>Options (comma separated)</label>
          <br />
          <textarea
            value={options}
            onChange={(e) => setOptions(e.target.value)}
            placeholder="iPhone 16, Samsung S26"
            rows={4}
            col={40}
          />
        </div>

        <br />

        <button type="submit">
          Create Decision
        </button>
      </form>
    </div>
  );
}

export default CreateDecision;