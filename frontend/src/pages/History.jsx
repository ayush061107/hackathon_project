function History() {
  const history = [
    {
      title: "Which phone should I buy?",
      winner: "iPhone 16",
    },
    {
      title: "Best Laptop",
      winner: "MacBook Air M4",
    },
  ];

  return (
    <div style={{ padding: "30px" }}>
      <h1>Decision History</h1>

      {history.map((item, index) => (
        <div
          key={index}
          style={{
            border: "1px solid #ccc",
            padding: "15px",
            marginTop: "15px",
            borderRadius: "8px",
         }}
        >
          <h3>{item.title}</h3>
          <p>Winner: {item.winner}</p>
        </div>
      ))}
    </div>
  );
}

export default History;