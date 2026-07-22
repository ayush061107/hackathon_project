import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "Arial",
        background: "#f5f5f5",
        minHeight: "100vh",
      }}
    >
      <h1>🛍️ Smart Product Decision Dashboard</h1>
      <p>Welcome to your Hackathon Project</p>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "15px",
          marginTop: "30px",
        }}
      >
        <Link to="/create-decision">
          <button>Create Decision</button>
        </Link>

        <Link to="/compare-products">
          <button>Compare Products</button>
        </Link>

        <Link to="/history">
          <button>History</button>
        </Link>

        <Link to="/login">
          <button>Login</button>
        </Link>

        <Link to="/register">
          <button>Register</button>
        </Link>
      </div>
    </div>
  );
}