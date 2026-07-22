import "./CompareProducts.css";
import products from "../data/Products.js";
import ProductCard from "../components/ProductCard";
import ComparisonTable from "../components/ComparisonTable";
import WinnerCard from "../components/WinnerCard";

function CompareProducts() {
  return (
    <div className="compare-page">
      <h1 className="compare-title">Compare Products</h1>

      <div className="product-row">
        <ProductCard product={products[0]} />
        <ProductCard product={products[1]} />
     </div>

      <ComparisonTable
        product1={products[0]}
        product2={products[1]}
      />

      <WinnerCard
        winner={products[0]}
        confidence="95%"
      />
    </div>
  );
}

export default CompareProducts;