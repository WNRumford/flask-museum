from app import app
from flask import render_template, url_for
from data import news, slideshow, afishi


@app.route('/')
def index():
    title = "Главная"
    n = news
    slides = slideshow
    return render_template('index.html', t=title, n=n, slides=slides)

@app.route('/news')
def all_news():
    title = 'Архивы новостей'
    return render_template('news.html', t=title)

@app.route('/afisha')
def afisha():
    title = 'Афиша'
    af = afishi
    return render_template('afisha.html', t=title, af=af)

@app.route('/gallery')
def gallery():
    title = 'Галерея'
    return render_template('gallery.html', t=title)
