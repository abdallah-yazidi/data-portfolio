import joblib
import os

MODEL_PATH = "model/model.pkl"

def load_model():
    """Charge le modele depuis le disque."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Modele non trouve a {MODEL_PATH}. "
            "Executez d'abord 'python train_model.py'."
        )
    
    model = joblib.load(MODEL_PATH)
    print(f"Modele charge depuis {MODEL_PATH}")
    return model

# Chargement unique au demarrage du module
model = load_model()