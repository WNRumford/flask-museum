from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    title = "Главная"
    return render_template('index.html', t=title)