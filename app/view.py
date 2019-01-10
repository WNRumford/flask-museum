from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    name = "Бобруйский художественный музей"
    return render_template('index.html', n=name)