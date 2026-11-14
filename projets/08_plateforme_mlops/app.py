from fastapi import FastAPI, HTTPException
from model_loader import model
from schemas import PredictionRequest, PredictionResponse
import pandas as pd

app = FastAPI(
    title="API de Prediction ML",
    description="API pour predire le churn client avec un modele Random Forest",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Endpoint racine pour verifier que l'API fonctionne."""
    return {
        "message": "API de Prediction ML est en ligne",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health_check():
    """Endpoint de sante pour le monitoring."""
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    """Endpoint de prediction."""
    try:
        input_data = pd.DataFrame([data.dict()])
        prediction = int(model.predict(input_data)[0])
        probability = float(model.predict_proba(input_data)[0][1])
        
        return PredictionResponse(
            prediction=prediction,
            probability_class_1=probability,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))