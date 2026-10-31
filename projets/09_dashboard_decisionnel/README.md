# Projet 9 : Dashboard Décisionnel E-commerce (Olist)

## Objectif
Analyser les performances de vente d'une plateforme e-commerce brésilienne (Olist) et créer un dashboard interactif pour le suivi des KPIs.

## Questions Business
1. Quelle est l'évolution du Chiffre d'Affaires mensuel ?
2. Quelles sont les catégories de produits les plus rentables ?
3. Quelle est la répartition géographique des clients ?
4. Quels sont les moyens de paiement privilégiés ?

## Dataset
Source : [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 100k commandes
- 30k clients
- 3k vendeurs
- Données de 2016 à 2018

## Stack Technique
- **Langage** : Python
- **Analyse** : Pandas, NumPy
- **Visualisation** : Plotly Express
- **Dashboard** : Streamlit

## Installation et Lancement

1. Installer les dépendances :
```bash
pip install -r requirements.txt

Lancer le dashboard interactif :
streamlit run dashboard.py

Le dashboard s'ouvrira automatiquement dans votre navigateur sur http://localhost:8501.
KPIs Suivis
Chiffre d'Affaires Total
Panier Moyen
Nombre de Commandes
Nombre de Clients
Commandes par Client
Visualisations
Évolution mensuelle du CA
Top 10 catégories de produits
Répartition géographique par état
Distribution des montants de commandes
Répartition des moyens de paiement
