import sqlite3

conn = sqlite3.connect('./recipes.db')
c = conn.cursor()


c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS ingredients
             USING FTS5(id, keywords);''')

c.execute('''INSERT INTO ingredients SELECT id,keywords FROM recipes;''')

conn.commit()
conn.close()