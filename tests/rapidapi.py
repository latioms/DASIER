# Scrapping data from a known rapidapi api and save them in a sqlite database

import requests
import json
import sqlite3

# Rapidapi api url
url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/524"

# Rapidapi api key
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "80c25ee547mshc87e5515e77eed9p18d68ajsnc8486dcc28c3"
    }

# Requesting data from the api
response = requests.request("GET", url, headers=headers)

# Converting the response to json
data = response.json()

# Creating a sqlite database
conn = sqlite3.connect('football.db')
c = conn.cursor()

# Creating a table
c.execute('''CREATE TABLE IF NOT EXISTS teams
                (id integer, name text, logo text, country text, founded integer, venue_name text, venue_surface text, venue_address text, venue_city text, venue_capacity integer)''')
print(data)
# Inserting data into the table
# for team in data['api']['teams']:
    # c.execute("INSERT INTO teams VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (team['team_id'], team['name'], team['logo'], team['country'], team['founded'], team['venue_name'], team['venue_surface'], team['venue_address'], team['venue_city'], team['venue_capacity']))

# Commiting the changes
conn.commit()
