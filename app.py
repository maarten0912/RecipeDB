import recipesdatabase.dbhelper as db
import json
import algorithm
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/help')
def help_page():
    return render_template('explanation.html')


@app.route('/swipe', methods=['POST'])
def swipe_page():
    ids = request.form['ids']
    swipes = request.form['swipes']
    back_num = request.form['back']
    if back_num == '1':
        back = True
    else:
        back = False
    if back:
        id_list = ids.split(",")
        swipes_list = swipes.split(",")
        ids = ''
        swipes = ''
        for i in range(len(id_list)-1):
            if i == 0:
                ids = id_list[i]
            else:
                ids += ','+id_list[i]

        for j in range(len(swipes_list)-1):
            if j == 0:
                swipes = swipes_list[j]
            else:
                swipes += ',' + swipes_list[j]

        next_id = id_list[len(id_list)-1]
        next_recipe = json.loads(db.get_recipe(next_id))

    else:
        print(ids)
        print(swipes)
        id_list = ids.split(",")
        swipe_list = swipes.split(",")

        # Use this if statement if the required amount of yes swipes needs to be above 5
        # if sum(map(lambda x: x == "yes", swipe_list)) >= 5:
        #     recipes = algorithm.getbestrecipes(id_list, swipe_list)
        #     return render_template('swipe.html', done=True, best_matches=recipes)

        # Use this if statement if the required amount of swipes need to be above 20
        if len(swipe_list) == 20:
            recipes = algorithm.getbestrecipes(id_list, swipe_list)
            return render_template('swipe.html', done=True, best_matches=recipes)

        next_id = db.get_random_id(done_ids=id_list)
        next_recipe = json.loads(db.get_recipe(next_id))

    return render_template('swipe.html', done=False, next_id=next_id, next_recipe=next_recipe, previous_ids=ids,
                           previous_swipes=swipes, current_id='')
