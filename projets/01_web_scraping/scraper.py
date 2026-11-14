import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_data():
    print("1. Connexion a la page web...")
    url = "https://www.scrapethissite.com/pages/forms/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur: Code de statut {response.status_code}")
        return
    
    print("2. Parsing du contenu HTML avec BeautifulSoup...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    rows = soup.find_all('tr', class_='team')
    
    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 9:
            team_data = {
                "Name": cols[0].text.strip(),
                "Year": int(cols[1].text.strip()),
                "Wins": int(cols[2].text.strip()),
                "Losses": int(cols[3].text.strip()),
                "OT_Losses": int(cols[4].text.strip()) if cols[4].text.strip() else 0,
                "Win_Percent": float(cols[6].text.strip()),
                "Goals_For": int(cols[7].text.strip()),
                "Goals_Against": int(cols[8].text.strip())
            }
            data.append(team_data)
    
    print(f"3. {len(data)} enregistrements extraits avec succes.")
    
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("data/hockey_teams.csv", index=False)
    print("4. Donnees sauvegardees dans data/hockey_teams.csv")
    
    return df

if __name__ == "__main__":
    scrape_data()