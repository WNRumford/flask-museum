from app import app
from flask import render_template, url_for
from data import news
from datetime import datetime

@app.route('/')
def index():
    title = "Главная"
    n = news
    return render_template('index.html', t=title, n=n)
