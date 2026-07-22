import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import CreateDecision from "./pages/CreateDecision";
import CompareProducts from "./pages/CompareProducts";
import History from "./pages/History";
import Login from "./pages/Login";
import Register from "./pages/Register";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/create-decision" element={<CreateDecision />} />
      <Route path="/compare-prodcts" element={<CompareProducts />} />
      <Route path="/history" element={<History />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;