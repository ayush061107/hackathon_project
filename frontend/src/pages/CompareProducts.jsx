import React from "react";

function CompareProducts() {
  const products = [
    {
      name: "iPhone 16",
      price: "₹79,999",
      camera: "48 MP",
      battery: "3561 mAh",
    },
    {
      name: "Samsung Galaxy S26",
      price: "₹74,999",
      camera: "50 MP",
      battery: "4500 mAh",
    },
  ];

  const cell = {
    border: "1px solid black",
    padding: "10px",
    textAlign: "center",
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Compare Products</h1>

      <table>
        style={{
          borderCollapse: "collapse",
          width: "600px",
          marginTop: "20px",
        }}
        
        <thead>
          <tr>
            <th style={cell}>Feature</th>
            <th style={cell}>{products[0].name}</th>
            <th style={cell}>{products[1].name}</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td style={cell}>Price</td>
            <td style={cell}>{products[0].price}</td>
            <td style={cell}>{products[1].price}</td>
          </tr>

          <tr>
            <td style={cell}>Camera</td>
            <td style={cell}>{products[0].camera}</td>
            <td style={cell}>{products[1].camera}</td>
          </tr>

          <tr>
            <td style={cell}>Battery</td>
            <td style={cell}>{products[0].battery}</td>
            <td style={cell}>{products[1].battery}</td>
          </tr>
        </tbody>
      </table>

      <h2 style={{ color: "green", marginTop: "20px" }}>
        Winner: iPhoe 16 🏆
      </h2>
    </div>
  );
}

export default CompareProducts;