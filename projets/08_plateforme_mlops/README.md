# Projet 8 : Plateforme MLOps - Déploiement de Modèle ML

## Objectif
Exposer un modèle de Machine Learning via une API REST performante (FastAPI) et conteneuriser l'application avec Docker pour un déploiement reproductible en production.

## Architecture Modulaire
- **train_model.py** : Entraîne et sauvegarde le modèle (Random Forest).
- **model_loader.py** : Charge le modèle depuis le disque.
- **schemas.py** : Définit les schémas de validation (Pydantic).
- **app.py** : API FastAPI avec endpoints `/`, `/health` et `/predict`.
- **Dockerfile** : Conteneurisation de l'application.

## Stack Technique
- **FastAPI** : Framework web moderne et rapide.
- **Uvicorn** : Serveur ASGI haute performance.
- **Pydantic** : Validation des données d'entrée/sortie.
- **Scikit-Learn** : Modèle de Machine Learning.
- **Docker** : Conteneurisation pour la production.

## Installation et Lancement (Local)

### 1. Installer les dépendances
```bash
pip install -r requirements.txt