import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute(
    "INSERT INTO registrants (name, sport) VALUES (?, ?)", ("Frankie", "Basketball")
)

cur.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", ("Silvie", "Soccer"))

connection.commit()
connection.close()
