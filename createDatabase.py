import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

createTable = "CREATE TABLE IF NOT EXISTS plates (plate_id text primary key, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"

cursor.execute(createTable)

connection.commit()
connection.close()