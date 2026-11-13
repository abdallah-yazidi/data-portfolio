import pandas as pd
from extract import extract
from transform import transform
from load import load

def main():
    """
    Orchestre l'execution du pipeline ETL complet.
    """
    print("=" * 60)
    print("DEBUT DU PIPELINE ETL")
    print("=" * 60)
    
    # Etape 1 : Extract
    df_raw = extract()
    
    # Etape 2 : Transform
    dim_customer, dim_product, fact_sales = transform(df_raw)
    
    # Etape 3 : Load
    load(dim_customer, dim_product, fact_sales)
    
    print("=" * 60)
    print("PIPELINE ETL TERMINE AVEC SUCCES !")
    print("=" * 60)

if __name__ == "__main__":
    main()