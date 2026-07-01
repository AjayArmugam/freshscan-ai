from fastapi import APIRouter, File, HTTPException, UploadFile
from PIL import Image

from backend.schemas.prediction import PredictionResponse
from backend.services.predictor import predictor

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
async def predict(file: UploadFile = File(...)):

    try:

        image = Image.open(file.file)

        result = predictor.predict(image)

        return PredictionResponse(**result)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )