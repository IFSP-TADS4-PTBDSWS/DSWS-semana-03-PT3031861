# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', name=username)

@app.route('/rotainexistente')
def not_found_route():
    return render_template('404.html'), 404



