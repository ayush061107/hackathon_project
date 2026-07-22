import "./ProductCard.css";

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <h2>{product.name}</h2>

      <p><strong>Price:</strong> ₹{product.price}</p>

      <p><strong>Rating:</strong> {product.rating}</p>

      <p><strong>Battery:</strong> {product.battery}</p>
    </div>
  );
}

export default ProductCard;