import "./WinnerCard.css";

function WinnerCard({ winner, confidence }) {
  return (
    <div className="winner-card">
      <h2>🏆 Recommended Product</h2>

      <h3>{winner.name}</h3>

      <p>Confidence: {confidence}</p>
    </div>
  );
}

export default WinnerCard;