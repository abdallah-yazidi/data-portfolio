# Projet 3 : Data Lakehouse avec Architecture Medallion

## Objectif
Construire un Data Lakehouse moderne en utilisant le format Delta Lake, en appliquant l'architecture Medallion (Bronze, Silver, Gold) pour garantir la qualité, la traçabilité et la performance des données.

## Architecture Medallion
- **Bronze (Raw)** : Données brutes ingérées telles quelles, avec historique complet et immuable.
- **Silver (Cleansed)** : Données nettoyées, filtrées (suppression des retours/erreurs) et typées, prêtes pour l'analyse.
- **Gold (Aggregated)** : Données agrégées au niveau business, optimisées pour les dashboards et le Machine Learning.

## Dataset
Source : [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/dataset/352/online+retail)
- Données de transactions d'un magasin en ligne britannique.

## Stack Technique
- **Python & Pandas** : Manipulation et transformation des données.
- **Delta Lake** : Format de table open-source avec garanties de transactions ACID.
- **PyArrow** : Moteur de lecture/écriture colonnaire pour des performances optimales.

## Résultats du Pipeline
- **Bronze** : 541 909 lignes brutes ingérées.
- **Silver** : 531 285 lignes nettoyées et validées.
- **Gold** : 38 lignes agrégées (KPIs par pays : Chiffre d'affaires, Nombre de commandes, Panier moyen).

## Structure du Projet
```text
03_data_lakehouse/
├── data/                  # (Non versionné) Données sources brutes
├── delta_lake/            # (Non versionné) Tables Delta générées (Bronze, Silver, Gold)
├── build_lakehouse.py     # Script principal du pipeline ETL
├── requirements.txt       # Dépendances Python
└── README.md              # Ce fichier

Installation et Lancement

# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Exécuter le pipeline
python build_lakehouse.py