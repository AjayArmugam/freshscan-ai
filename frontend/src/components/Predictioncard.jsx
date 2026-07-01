import "../styles/PredictionCard.css";

import { predictImage } from "../services/api";

const CLASS_NAMES = {
  freshapples: "Fresh Apple",
  rottenapples: "Rotten Apple",

  freshbanana: "Fresh Banana",
  rottenbanana: "Rotten Banana",

  freshoranges: "Fresh Orange",
  rottenoranges: "Rotten Orange",

  freshpotato: "Fresh Potato",
  rottenpotato: "Rotten Potato",

  freshtomato: "Fresh Tomato",
  rottentomato: "Rotten Tomato",

  freshokra: "Fresh Okra",
  rottenokra: "Rotten Okra",

  freshcucumber: "Fresh Cucumber",
  rottencucumber: "Rotten Cucumber",
};

function PredictionCard({
  selectedImage,
  prediction,
  setPrediction,
  loading,
  setLoading,
}) {
  const handlePredict = async () => {
    if (!selectedImage) return;

    try {
      setLoading(true);

      const result = await predictImage(selectedImage);

      setPrediction(result);
    } catch (error) {
      console.error(error);
      alert("Prediction failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="prediction-card">
      <h2>AI Prediction</h2>

      {prediction ? (
        <>
          <div className="prediction-result">
            <h3>{CLASS_NAMES[prediction.prediction] || prediction.prediction}</h3>

            <p>
              Confidence: <strong>{prediction.confidence}%</strong>
            </p>
          </div>
        </>
      ) : (
        <div className="prediction-result">
          <h3>No Prediction Yet</h3>
          <p>Select an image and click Predict.</p>
        </div>
      )}

      <button
        className="predict-btn"
        onClick={handlePredict}
        disabled={!selectedImage || loading}
      >
        {loading ? "Predicting..." : "Predict Freshness"}
      </button>
    </div>
  );
}

export default PredictionCard;