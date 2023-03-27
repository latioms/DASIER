#  select all elements in population table and print them

import sqlite3
conn = sqlite3.connect('population.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM population")
print(cursor.fetchall())
