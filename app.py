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
        ingredient_list = []
        for i in range(len(id_list)):
            if swipe_list[i] == "yes":
                ingredient_list.extend(json.loads(db.get_recipe(id_list[i]))["simple_ingredients"])
        #
        # ingredient_list, values = algorithm.calculateingredientscores(id_list, swipe_list, 5)
        # algorithm.getbestrecipes(id_list, swipe_list)
        #
        matches = db.best_matches(ingredient_list=ingredient_list)
        recipes = []
        for match in matches:
            recipes.append(json.loads(db.get_recipe(match[0])))
        # Dit gedeelte zorgt ervoor dat de scores worden gebruikt om de beste recepten weer te geven
        recipes = algorithm.getbestrecipes(id_list, swipe_list)
        #
        return render_template('swipe.html', done=True, best_matches=recipes)

    next_id = db.get_random_id(done_ids=id_list)
    next_recipe = json.loads(db.get_recipe(next_id))

    return render_template('swipe.html', done=False, next_id=next_id, next_recipe=next_recipe, previous_ids=ids,
                           previous_swipes=swipes)
