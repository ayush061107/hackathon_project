import "./CreateDecision.css";
import { useState } from "react";

function CreateDecision() {
  const [decision, setDecision] = useState("");
  const [options, setOptions] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    alert("Decision Created!");

    console.log({
      decision,
      options: options.split(","),
    });

    setDecision("");
    setOptions("");
  };

  return (
    <div className="decision-container">
      <h1>Create Decision</h1>

      <form onSubmit={handleSubmit}>
        <label>ecision Title</label>
        <input
          type="text"
          placeholder="Example: Which phone should I buy?"
          value={decision}
          onChange={(e) => setDecision(e.target.value)}
          required
        />

        <label>Options (comma separated)</label>
        <textarea
          placeholder="iPhone 16, Samsung S26, OnePlus 14"
          value={options}
          onChange={(e) => setOptions(e.target.value)}
          required
        />

        <button type="submit">
         Create Decision
        </button>
      </form>
    </div>
  );
}

export default CreateDecision;