import "../styles/ImageUploader.css";

function ImageUploader({ selectedImage, setSelectedImage }) {
  const handleChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setSelectedImage(file);
    }
  };

  return (
    <div className="upload-card">

      <label htmlFor="image-upload" className="upload-area">

        <div className="upload-icon">📤</div>

        <h2>Upload Food Image</h2>

        <p>Click here or Drag & Drop an image</p>

        <span>JPG • JPEG • PNG Supported</span>

      </label>

      <input
        id="image-upload"
        type="file"
        accept="image/*"
        onChange={handleChange}
        hidden
      />

    </div>
  );
}

export default ImageUploader;