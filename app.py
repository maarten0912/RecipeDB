from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/swipe', methods=['POST'])
def swipe_page():
    return render_template('swipe.html')