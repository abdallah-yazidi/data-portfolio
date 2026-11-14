from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    """Schema de la requete de prediction."""
    age: int = Field(..., ge=18, le=100, description="Age du client")
    income: float = Field(..., ge=0, description="Revenu annuel en euros")
    months_active: int = Field(..., ge=1, le=120, description="Mois d'activite")

class PredictionResponse(BaseModel):
    """Schema de la reponse de prediction."""
    prediction: int
    probability_class_1: float
    status: str