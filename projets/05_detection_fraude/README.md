# Projet 5 : Détection de Fraude Bancaire

## Objectif
Détecter les transactions frauduleuses dans un dataset fortement déséquilibré (0.17% de fraudes) en minimisant les faux positifs.

## Questions Business
1. Comment détecter les fraudes avec un taux de faux positifs minimal ?
2. Quel algorithme gère le mieux le déséquilibre de classes ?
3. Quelles features sont les plus déterminantes pour la détection ?

## Dataset
Source : [Credit Card Fraud Detection (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 284 807 transactions
- 492 fraudes (0.172%)
- 30 variables anonymisées (PCA) + Time + Amount

## Méthodologie
- **Prétraitement** : Standardisation des montants et du temps.
- **Gestion du déséquilibre** : SMOTE (Synthetic Minority Over-sampling Technique).
- **Modèles comparés** : Logistic Regression (Baseline), Random Forest, XGBoost.
- **Métriques** : Precision, Recall, F1-Score, AUC-ROC, PR-AUC.
- **Interprétabilité** : SHAP values pour expliquer les prédictions du modèle.
- **MLOps** : Tracking des expériences avec MLflow.

## Installation
```bash
pip install -r requirements.txt