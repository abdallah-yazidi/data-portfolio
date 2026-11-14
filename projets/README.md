# Projet 1 : Web Scraping et Analyse Exploratoire

## Objectif
Démontrer la capacité à extraire des données non structurées depuis le web, à les structurer en format tabulaire, et à en tirer des insights business via une analyse exploratoire (EDA).

## Méthodologie
1. **Extraction** : Utilisation de `requests` et `BeautifulSoup4` pour parser une page HTML et récupérer les données brutes.
2. **Structuration** : Conversion des données extraites en DataFrame Pandas et sauvegarde en CSV.
3. **Analyse** : Nettoyage des données et visualisation des tendances clés avec Matplotlib et Seaborn.

## Dataset
- Source : [Scrape This Site (Hockey Teams)](https://www.scrapethissite.com/pages/forms/)
- Contenu : Statistiques de 25 équipes de hockey sur glace (victoires, défaites, buts marqués/encaissés, pourcentage de victoire).

## Stack Technique
- Python, Requests, BeautifulSoup4
- Pandas (Manipulation de données)
- Matplotlib / Seaborn (Visualisation)

## Résultats
- Extraction réussie de 25 enregistrements structurés.
- Identification des 10 équipes les plus victorieuses.
- Analyse de la corrélation entre les buts marqués et le pourcentage de victoire.

## Installation et Lancement

### 1. Installer les dépendances
```bash
pip install -r requirements.txt

2. Lancer le script de scraping
python scraper.py


3. Lancer l'analyse
jupyter notebook
