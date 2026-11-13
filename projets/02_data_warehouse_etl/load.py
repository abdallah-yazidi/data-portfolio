import pandas as pd
import sqlite3
import os

def load(dim_customer, dim_product, fact_sales):
    """
    Charge les tables de dimensions et de faits dans une base SQLite.
    """
    db_path = 'data/warehouse.db'
    
    print(f"Load: Connexion a la base {db_path}...")
    
    # Supprimer l'ancienne base si elle existe
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    
    # Charger les tables dans SQLite
    dim_customer.to_sql('dim_customer', conn, index=False, if_exists='replace')
    dim_product.to_sql('dim_product', conn, index=False, if_exists='replace')
    fact_sales.to_sql('fact_sales', conn, index=False, if_exists='replace')
    
    conn.close()
    print("Load: Donnees chargees avec succes dans le Data Warehouse.")