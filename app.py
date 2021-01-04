import recipesdatabase.dbhelper as db
import json
import algorithm
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/swipe', methods=['POST'])
def swipe_page():
    ids = request.form['ids']
    swipes = request.form['swipes']
    id_list = ids.split(",")
    swipe_list = swipes.split(",")

    if sum(map(lambda x: x == "yes", swipe_list)) >= 5:
        recipes = algorithm.getbestrecipes(id_list, swipe_list)
        return render_template('swipe.html', done=True, best_matches=recipes)

    next_id = db.get_random_id(done_ids=id_list)
    next_recipe = json.loads(db.get_recipe(next_id))

    return render_template('swipe.html', done=False, next_id=next_id, next_recipe=next_recipe, previous_ids=ids,
                           previous_swipes=swipes)
