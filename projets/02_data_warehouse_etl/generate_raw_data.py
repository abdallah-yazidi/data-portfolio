import pandas as pd
import os

os.makedirs('data', exist_ok=True)

print("Lecture du fichier Online Retail.xlsx...")
df_raw = pd.read_excel('data/Online Retail.xlsx')

print(f"Dataset charge : {len(df_raw)} lignes")
print(f"Colonnes : {df_raw.columns.tolist()}")
print(f"\nApercu des donnees :")
print(df_raw.head())
print(f"\nValeurs nulles par colonne :")
print(df_raw.isnull().sum())

df_raw.to_csv('data/raw_sales.csv', index=False)
print("\nDonnees brutes sauvegardees dans data/raw_sales.csv")