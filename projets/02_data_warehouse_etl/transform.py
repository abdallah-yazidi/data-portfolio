import pandas as pd

def transform(df):
    """
    Nettoie les donnees brutes et cree les tables de dimensions et de faits.
    """
    print("Transform: Debut du nettoyage...")
    
    # Supprimer les lignes avec InvoiceNo ou StockCode nul
    df = df.dropna(subset=['InvoiceNo', 'StockCode']).copy()
    
    # Supprimer les factures de remboursement (commencant par C)
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')].copy()
    
    # Filtrer les quantites et prix positifs
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)].copy()
    
    # Nettoyer la description
    df['Description'] = df['Description'].fillna('Unknown')
    df = df[df['Description'].str.strip() != ''].copy()
    
    # Calculer le montant total
    df['total_amount'] = df['Quantity'] * df['UnitPrice']
    
    # Convertir la date
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['date'] = df['InvoiceDate'].dt.date
    
    # Creer la dimension Client
    dim_customer = df[['CustomerID']].dropna().drop_duplicates().reset_index(drop=True)
    dim_customer['customer_id'] = dim_customer.index + 1
    
    # Creer la dimension Produit
    dim_product = df[['StockCode', 'Description', 'UnitPrice']].drop_duplicates().reset_index(drop=True)
    dim_product['product_id'] = dim_product.index + 1
    
    # Creer la table de Faits avec les cles etrangeres
    fact_sales = df.merge(dim_customer, on='CustomerID', how='left')
    fact_sales = fact_sales.merge(dim_product, on=['StockCode', 'Description', 'UnitPrice'], how='left')
    
    # Selectionner les colonnes finales
    fact_sales = fact_sales[[
        'InvoiceNo', 'date', 'customer_id', 'product_id', 
        'Quantity', 'total_amount', 'Country'
    ]].copy()
    
    print(f"Transform: {len(fact_sales)} transactions apres nettoyage.")
    print(f"Transform: {len(dim_customer)} clients uniques.")
    print(f"Transform: {len(dim_product)} produits uniques.")
    print("Transform: Nettoyage et structuration termines.")
    
    return dim_customer, dim_product, fact_sales