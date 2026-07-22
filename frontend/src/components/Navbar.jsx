import { Link, useLocation } from "react-router-dom";
import { FaMoon, FaSun } from "react-icons/fa";
import { useTheme } from "../context/ThemeContext";
import "./Navbar.css";

export default function Navbar() {
  const { darkMode, setDarkMode } = useTheme();
  const location = useLocation();

  const active = (path) => (location.pathname === path ? "active" : "");

  return (
    <nav className="navbar">
      <div className="logo">
        Decision<span>Flow</span>
      </div>

      <div className="av-links">
        <Link className={active("/")} to="/">
          Dashboard
        </Link>

        <Link className={active("/create-decision")} to="/create-decision">
          Create Decision
        </Link>

        <Link className={active("/compare-products")} to="/compare-products">
          Compare Products
        </Link>

        <Link className={active("/history")} to="/history">
          History
        </Link>

        <Link className={active("/login")} to="/login">
          Login
       </Link>

        <Link className={active("/register")} to="/register">
          Register
        </Link>
      </div>

      <button
        className="theme-btn"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? <FaSun /> : <FaMoon />}
      </button>
    </nav>
  );
}