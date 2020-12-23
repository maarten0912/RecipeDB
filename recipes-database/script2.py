import sqlite3

ingredients = input("What ingredients do you like?\n> ")

conn = sqlite3.connect('./recipes.db')
c = conn.cursor()

c.execute('''SELECT *
             FROM ingredients
             WHERE ingredients MATCH ?
             ORDER BY rank
             LIMIT 20''',[ingredients])

rows = c.fetchall()

print("")
for row in rows:
    print(row)

print("")
number = input("Enter the number of the recipe you want to view:\n> ")

c.execute('''SELECT *
             FROM recipes
             WHERE id = ?''',[int(number)])

rows = c.fetchall()

print("")
for row in rows:
    print(row)

conn.commit()
conn.close()