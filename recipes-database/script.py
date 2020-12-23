import sqlite3
import pyquery
import sys
from tqdm import tqdm
import os
from pyquery import PyQuery as pq
import json

conn = sqlite3.connect('./recipes.db')
c = conn.cursor()

try:
    folder = sys.argv[1]
except:
    print("Usage: python script.js <recipefolder>")
    exit()

filelist = os.listdir(folder)
for entry in tqdm(filelist):
    counter = len(filelist)
    with open(os.path.join(folder,entry)) as f:
        html = f.read()
    d = pq(html)
    recipe = {}
    recipe['title'] = d('h1.content-title__text').text()
    recipe['ingredients'] = []
    recipe['simple_ingredients'] = []
    for item in d('.recipe-ingredients__list li').items():
        if item.text() != "":
            recipe['ingredients'].append(item.text())
            if len(item.children()) > 0:
                recipe['simple_ingredients'].append(item.children().text())
    recipe['method'] = []
    for item in d('.recipe-method__list li p').items():
        recipe['method'].append(item.text())
    recipe['time'] = {
        "prep": d('.recipe-metadata__prep-time').eq(0).text(),
        "cook": d('.recipe-metadata__cook-time').eq(0).text()
    }
    recipe['serves'] = d('.recipe-metadata__serving').eq(0).text()[7:]
    recipe['image'] = d('.recipe-media__image img').attr['src']


    c.execute('''INSERT OR IGNORE INTO recipes(recipe, keywords) VALUES(?, ?)''',[json.dumps(recipe),json.dumps(recipe['simple_ingredients'])])


conn.commit()
conn.close()