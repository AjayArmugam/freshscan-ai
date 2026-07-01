import "../styles/ImagePreview.css";

function ImagePreview({ selectedImage }) {

  return (

    <div className="preview-card">

      <h2>Image Preview</h2>

      {
        selectedImage ? (

          <img
            src={URL.createObjectURL(selectedImage)}
            alt="preview"
          />

        ) : (

          <div className="empty-preview">

            No Image Selected

          </div>

        )
      }

    </div>

  );
}

export default ImagePreview;