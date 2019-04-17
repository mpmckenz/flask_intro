from flask import Flask
from flask import render_template
from tinydb import TinyDB, Query
from jinja2 import Template
import random

app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def index(name=None):
    recipe = random.choice(db.all())
    return render_template('hello.html', name=recipe)
