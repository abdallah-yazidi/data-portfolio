# Projet 4 : Système de Recommandation de Films

## Objectif
Construire un moteur de recommandation de films basé sur le filtrage collaboratif pour prédire les préférences des utilisateurs.

## Questions Business
1. Quels films recommander à un utilisateur pour maximiser la probabilité de visionnage ?
2. Quels films sont les plus "similaires" en termes de goût des utilisateurs ?
3. Quelle est la performance du modèle de factorisation matricielle (SVD) ?

## Dataset
Source : [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)
- 100 000 notes (1 à 5 étoiles)
- 943 utilisateurs
- 1 682 films

## Méthodologie
- **Prétraitement** : Fusion des tables, encodage des IDs, création de la matrice Utilisateur-Item.
- **Modèle 1** : Similarité Cosinus (Item-Based Collaborative Filtering).
- **Modèle 2** : Factorisation de Matrice (Truncated SVD via Scikit-Learn).
- **Évaluation** : RMSE (Root Mean Square Error) sur un ensemble de test.
- **MLOps** : Tracking des performances avec MLflow.

## Installation
```bash
pip install -r requirements.txt