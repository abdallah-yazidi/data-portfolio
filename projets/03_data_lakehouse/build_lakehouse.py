import pandas as pd
import pyarrow as pa
import os
from deltalake import write_deltalake, DeltaTable

LAKE_PATH = "delta_lake"

def create_bronze():
    print("1. Creation de la couche Bronze...")
    
    csv_path = "data/Online Retail.xlsx"
    
    if os.path.exists(csv_path):
        df_bronze = pd.read_excel(csv_path)
        print(f"   Lecture du fichier brut : {len(df_bronze)} lignes.")
    else:
        print("   Fichier brut non trouve, generation de donnees de test...")
        df_bronze = pd.DataFrame({
            "InvoiceNo": ["INV001", "INV002", "INV003", "INV004"],
            "StockCode": ["A1", "B2", "A1", "C3"],
            "Description": ["Laptop", "Mouse", "Laptop", "Keyboard"],
            "Quantity": [1, 2, -1, 5],
            "InvoiceDate": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
            "UnitPrice": [1000.0, 25.0, 1000.0, 50.0],
            "CustomerID": [101, 102, None, 101],
            "Country": ["France", "Germany", "France", "Spain"]
        })

    # Conversion explicite de TOUTES les colonnes pour eviter les conflits de types PyArrow
    df_bronze["InvoiceNo"] = df_bronze["InvoiceNo"].astype(str)
    df_bronze["StockCode"] = df_bronze["StockCode"].astype(str)
    df_bronze["Description"] = df_bronze["Description"].fillna("").astype(str)
    df_bronze["Quantity"] = pd.to_numeric(df_bronze["Quantity"], errors="coerce").fillna(0).astype(int)
    df_bronze["InvoiceDate"] = df_bronze["InvoiceDate"].astype(str)
    df_bronze["UnitPrice"] = pd.to_numeric(df_bronze["UnitPrice"], errors="coerce").fillna(0.0).astype(float)
    df_bronze["CustomerID"] = df_bronze["CustomerID"].fillna("").astype(str)
    df_bronze["Country"] = df_bronze["Country"].fillna("").astype(str)

    bronze_path = os.path.join(LAKE_PATH, "bronze_sales")
    table = pa.Table.from_pandas(df_bronze)
    write_deltalake(bronze_path, table)
    print(f"   -> {len(df_bronze)} lignes ecrites dans Bronze.")
    return bronze_path

def create_silver(bronze_path):
    print("2. Creation de la couche Silver...")
    
    dt_bronze = DeltaTable(bronze_path)
    df_silver = dt_bronze.to_pandas()
    
    # Nettoyage
    df_silver = df_silver[df_silver["InvoiceNo"] != ""].copy()
    df_silver = df_silver[df_silver["StockCode"] != ""].copy()
    df_silver = df_silver[~df_silver["InvoiceNo"].str.startswith("C")].copy()
    df_silver = df_silver[df_silver["Quantity"] > 0].copy()
    df_silver["CustomerID"] = df_silver["CustomerID"].replace("", "UNKNOWN")
    df_silver["TotalAmount"] = df_silver["Quantity"] * df_silver["UnitPrice"]
    df_silver["InvoiceDate"] = pd.to_datetime(df_silver["InvoiceDate"], errors="coerce").dt.date
    
    # Conversion explicite
    df_silver["InvoiceNo"] = df_silver["InvoiceNo"].astype(str)
    df_silver["StockCode"] = df_silver["StockCode"].astype(str)
    df_silver["Description"] = df_silver["Description"].fillna("").astype(str)
    df_silver["CustomerID"] = df_silver["CustomerID"].astype(str)
    df_silver["Country"] = df_silver["Country"].fillna("").astype(str)
    df_silver["Quantity"] = df_silver["Quantity"].astype(int)
    df_silver["UnitPrice"] = df_silver["UnitPrice"].astype(float)
    df_silver["TotalAmount"] = df_silver["TotalAmount"].astype(float)

    silver_path = os.path.join(LAKE_PATH, "silver_sales")
    table = pa.Table.from_pandas(df_silver)
    write_deltalake(silver_path, table)
    print(f"   -> {len(df_silver)} lignes propres ecrites dans Silver.")
    return silver_path

def create_gold(silver_path):
    print("3. Creation de la couche Gold...")
    
    dt_silver = DeltaTable(silver_path)
    df_silver = dt_silver.to_pandas()
    
    df_gold = df_silver.groupby("Country").agg(
        Total_Revenue=("TotalAmount", "sum"),
        Total_Orders=("InvoiceNo", "nunique"),
        Avg_Basket_Size=("TotalAmount", "mean")
    ).reset_index()
    
    df_gold["Total_Revenue"] = df_gold["Total_Revenue"].round(2).astype(float)
    df_gold["Avg_Basket_Size"] = df_gold["Avg_Basket_Size"].round(2).astype(float)
    df_gold["Total_Orders"] = df_gold["Total_Orders"].astype(int)
    df_gold["Country"] = df_gold["Country"].astype(str)
    
    gold_path = os.path.join(LAKE_PATH, "gold_sales_by_country")
    table = pa.Table.from_pandas(df_gold)
    write_deltalake(gold_path, table)
    print(f"   -> {len(df_gold)} lignes agregees ecrites dans Gold.")
    return gold_path

def main():
    print("=" * 50)
    print("DEBUT DU PIPELINE DATA LAKEHOUSE (MEDALLION)")
    print("=" * 50)
    
    os.makedirs(LAKE_PATH, exist_ok=True)
    
    bronze = create_bronze()
    silver = create_silver(bronze)
    gold = create_gold(silver)
    
    print("=" * 50)
    print("PIPELINE LAKEHOUSE TERMINE AVEC SUCCES !")
    print("=" * 50)

if __name__ == "__main__":
    main()