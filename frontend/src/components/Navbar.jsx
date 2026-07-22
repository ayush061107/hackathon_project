import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav>
            <h2>DecisionFlow</h2>

            <Link to="/">
                <button>Dashboard</button>
            </Link>

            <Link to="/create-decision">
                <button>Create Decision</button>
            </Link>

            <Link to="/compare-Products">
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
        </nav>
    ) ;
}
export default Navbar;
