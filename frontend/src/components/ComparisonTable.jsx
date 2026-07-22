import "./ComparisonTable.css";

function ComparisonTable({ product1, product2 }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>{product1.name}</th>
          <th>{product2.name}</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Price</td>
          <td>₹{product1.price}</td>
          <td>₹{product2.price}</td>
        </tr>

        <tr>
          <td>Rating</td>
          <td>{product1.rating}</td>
          <td>{product2.rating}</td>
        </tr>

        <tr>
          <td>Battery</td>
          <td>{product1.battery}</td>
          <td>{product2.battery}</td>
        </tr>
      </tbody>
    </table>
  );
}

export default ComparisonTable;