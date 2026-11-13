# Projet 2 : Pipeline ETL et Data Warehouse

## Objectif
Construire un pipeline ETL modulaire et automatisé pour extraire des données de ventes brutes (540k+ transactions), les transformer et les charger dans un Data Warehouse relationnel (SQLite) avec un schéma en étoile.

## Questions Business
1. Comment structurer des données brutes pour permettre des analyses rapides ?
2. Comment automatiser le nettoyage et l'agrégation des données ?
3. Comment garantir l'intégrité des données lors du chargement ?

## Dataset
Source : [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/dataset/352/online+retail)
- 541 909 transactions d'un magasin en ligne britannique
- Période : 01/12/2010 - 09/12/2011
- 8 colonnes : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

## Architecture du Pipeline
- **Extract** (`extract.py`) : Lecture du fichier Excel brut et conversion en CSV.
- **Transform** (`transform.py`) : Nettoyage (suppression des remboursements, valeurs nulles), création des clés étrangères, agrégation du montant total.
- **Load** (`load.py`) : Insertion dans une base SQLite avec un schéma en étoile.
- **Orchestration** (`run_pipeline.py`) : Script principal qui exécute les 3 étapes dans l'ordre.

## Schéma en étoile (Star Schema)
- **dim_customer** : Table de dimension des clients (4 338 clients uniques).
- **dim_product** : Table de dimension des produits (15 810 produits uniques).
- **fact_sales** : Table de faits des ventes (530 104 transactions nettoyées).

## Stack Technique
- Python (Pandas pour la manipulation)
- SQLite (Data Warehouse local)
- openpyxl (Lecture de fichiers Excel)
- Schéma en étoile (Star Schema)

## Installation et Lancement
```bash
pip install -r requirements.txt
python run_pipeline.py

Résultats
541 909 lignes brutes → 530 104 transactions propres
4 338 clients uniques identifiés
15 810 produits uniques catalogués



---

##  Upload sur GitHub

1. Va sur GitHub dans ton dossier `projets/`
2. Clique sur **"Add file"** → **"Create new file"**
3. Nomme le fichier : `02_data_warehouse_etl/README.md`
4. Colle le nouveau README ci-dessus
5. Commit

6. Ensuite, dans le dossier `02_data_warehouse_etl`, clique sur **"Add file"** → **"Upload files"**
7. Glisse **uniquement** ces fichiers :
   -  `extract.py`
   -  `transform.py`
   -  `load.py`
   -  `run_pipeline.py`
   -  `requirements.txt`
8. Commit message : `feat: Projet 2 - Pipeline ETL modulaire avec Data Warehouse SQLite (Online Retail)`

---

**Dis-moi "Upload Projet 2 terminé "** quand c'est en ligne ! 🚀