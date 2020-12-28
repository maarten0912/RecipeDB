import sqlite3
import random

def get_random_id(done_ids):
    conn = sqlite3.connect('./recipes.db')
    c = conn.cursor()
    c.execute('''SELECT *
                FROM recipes''')

    all_ids = [row[0] for row in c.fetchall()]

    choose_ids = list(set(all_ids) - set(done_ids))

    conn.close()

    return random.choice(choose_ids)

def get_recipe(id):
    conn = sqlite3.connect('./recipes.db')
    c = conn.cursor()
    c.execute('''SELECT *
             FROM recipes
             WHERE id = ?''',[int(id)])

    rows = [row for row in c.fetchall()]

    conn.close()

    return rows[0][1] if len(rows) >= 1 else None

def best_matches(ingredient_list):
    search_query = " OR ".join(ingredient_list).replace("-","").replace("^","").replace(":","").replace("(","").replace(")","")

    conn = sqlite3.connect('./recipes.db')
    c = conn.cursor()

    c.execute('''SELECT *
                FROM ingredients
                WHERE ingredients MATCH ?
                ORDER BY rank''',[search_query])

    rows = c.fetchall()
    conn.close()

    return rows