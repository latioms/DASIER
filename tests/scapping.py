import sqlite3
import requests
from bs4 import BeautifulSoup

# Récupération du contenu HTML de la page
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Récupération des en-têtes de colonnes
headers = [header.text for header in soup.select("thead th")]

# Récupération des données de chaque ligne
rows = []
for row in soup.select("#example2 tbody tr"):
    data = [cell.text.strip().replace(",", "") for cell in row.select("td")]
    rows.append(data)

print(data)
# Création de la table et insertion des données dans une base de données SQLite
conn = sqlite3.connect('population.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS population
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT,
                population INTEGER,
                yearly_change FLOAT,
                net_change INTEGER,
                density INTEGER,
                land_area INTEGER,
                migrants INTEGER,
                fertility_rate FLOAT,
                median_age INTEGER,
                urban_pop_pct INTEGER,
                world_share FLOAT)''')
conn.commit()

# Insertion des données dans la table
for row in rows:
    # Conversion des données en types appropriés
    row[1] = row[1].replace(',', '')  # Suppression des virgules dans les nombres
    row[2] = float(row[2].strip('%'))  # Conversion en pourcentage
    row[3] = float(row[3].strip('%'))  # Conversion en pourcentage
    row[4] = int(row[4].replace(',', ''))  # Suppression des virgules dans les nombres
    row[5] = int(row[5].replace(',', ''))  # Suppression des virgules dans les nombres
    row[6] = int(row[6].replace(',', ''))  # Suppression des virgules dans les nombres
    row[7] = int(row[7].replace(',', ''))  # Suppression des virgules dans les nombres
    row[8] = float(row[8].replace(',', '.'))  # Conversion en décimal
    row[9] = int(row[9])  # Conversion en entier
    row[10] = int(row[10].strip('%'))  # Conversion en pourcentage
    row[11] = float(row[11].strip('%'))  # Conversion en pourcentage
    
    cursor.execute("INSERT INTO population (country, population, yearly_change, net_change, density, land_area, migrants, fertility_rate, median_age, urban_pop_pct, world_share) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row[1:])
    conn.commit()

conn.close()