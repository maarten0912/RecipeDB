import sqlite3

conn = sqlite3.connect('./recipes.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe TEXT UNIQUE,
                keywords TEXT
             );''')

conn.commit()
conn.close()