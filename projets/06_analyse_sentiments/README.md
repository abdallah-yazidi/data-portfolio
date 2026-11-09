# Projet 6 : Analyse de Sentiments (NLP)

## Objectif
Analyser automatiquement les avis de films IMDB pour détecter le sentiment (positif/négatif) et aider à la modération de contenu.

## Questions Business
1. Peut-on prédire automatiquement si un avis est positif ou négatif ?
2. Quel algorithme de NLP offre la meilleure précision ?
3. Quels mots influencent le plus la prédiction ?

## Dataset
Source : [IMDB Dataset (Kaggle)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- 50 000 avis de films
- 25 000 positifs / 25 000 négatifs
- Texte brut non structuré

## Méthodologie
- **Prétraitement** : Nettoyage du texte (lowercase, suppression HTML, stemming)
- **Vectorisation** : TF-IDF (Term Frequency-Inverse Document Frequency)
- **Modèles** : Naive Bayes, Logistic Regression, Random Forest
- **Métriques** : Accuracy, Precision, Recall, F1-Score
- **MLOps** : Tracking avec MLflow

## Installation
```bash
pip install -r requirements.txt