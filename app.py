import recipesdatabase.dbhelper as db
import json
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
    
    if len(id_list) >= 5:
        return render_template('swipe.html', done=True)

    next_id = db.get_random_id(done_ids=id_list)
    next_recipe = json.loads(db.get_recipe(next_id))

    return render_template('swipe.html', done=False, next_id=next_id, next_recipe=next_recipe, previous_ids=ids, previous_swipes=swipes)