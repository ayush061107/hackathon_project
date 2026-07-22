import { Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import History from "./pages/History";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ProductListing from "./pages/ProductListing";
import FilterProducts from "./pages/FilterProducts";
import PriorityWeights from "./pages/PriorityWeights";
import Recommendation from "./pages/Recommendation";
import CreateDecision from "./pages/CreateDecision";
import CompareProducts from "./pages/CompareProducts";
function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard/>} />
        <Route path="/create-decision" element={<CreateDecision />} />
        <Route path="/compare-products" element={<CompareProducts />} />
        <Route path="/history" element={<History/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="/prouduct-listing" element={<ProductListing/>} />
        <Route path="/flter-products" element={<FilterProducts/>} />
        <Route path="/priority-weights" element={<PriorityWeights/>} />
        <Route path="/recommendation" element={<Recommendation/>} />
      </Routes>
    </>
  );
}

export default App;