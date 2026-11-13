import pandas as pd
import os

def extract():
    """
    Extrait les donnees brutes du fichier Excel et les sauvegarde en CSV.
    """
    source_file = 'data/Online Retail.xlsx'
    output_file = 'data/raw_sales.csv'
    
    print(f"Extract: Lecture du fichier {source_file}...")
    df_raw = pd.read_excel(source_file)
    
    print(f"Extract: {len(df_raw)} lignes lues.")
    print(f"Extract: Colonnes detectees : {df_raw.columns.tolist()}")
    
    os.makedirs('data', exist_ok=True)
    df_raw.to_csv(output_file, index=False)
    
    print(f"Extract: Donnees brutes sauvegardees dans {output_file}")
    return df_raw

if __name__ == "__main__":
    extract()