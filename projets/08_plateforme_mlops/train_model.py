import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def generate_data():
    """Genere des donnees fictives pour la prediction de churn."""
    np.random.seed(42)
    n_samples = 1000
    
    X = pd.DataFrame({
        "age": np.random.randint(18, 70, n_samples),
        "income": np.random.randint(30000, 120000, n_samples),
        "months_active": np.random.randint(1, 60, n_samples)
    })
    y = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    
    return X, y

def train_and_save():
    """Entraîne le modele et le sauvegarde."""
    print("1. Generation des donnees d'entrainement...")
    X, y = generate_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("2. Entrainement du modele Random Forest...")
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"   Precision du modele : {accuracy:.4f}")
    
    print("3. Sauvegarde du modele...")
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("   Modele sauvegarde dans model/model.pkl")
    
    return accuracy

if __name__ == "__main__":
    train_and_save()