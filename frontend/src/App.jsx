import { useState } from "react";

import Header from "./components/Header";
import ImageUploader from "./components/ImageUploader";
import ImagePreview from "./components/ImagePreview";
import PredictionCard from "./components/PredictionCard";

import "./styles/App.css";

function App() {
  // Selected image
  const [selectedImage, setSelectedImage] = useState(null);

  // Prediction returned by FastAPI
  const [prediction, setPrediction] = useState(null);

  // Loading state while API is processing
  const [loading, setLoading] = useState(false);

  return (
    <div className="app">
      <Header />

      <div className="content">
        <ImageUploader
          selectedImage={selectedImage}
          setSelectedImage={setSelectedImage}
        />

        <div className="result-section">
          <ImagePreview selectedImage={selectedImage} />

          <PredictionCard
            selectedImage={selectedImage}
            prediction={prediction}
            setPrediction={setPrediction}
            loading={loading}
            setLoading={setLoading}
          />
        </div>
      </div>
    </div>
  );
}

export default App;