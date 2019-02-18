from flask import render_template
from app import app
from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    Business_news = get_source('business')
    Entertainment_news = get_source('entertainment')
    Sport_news = get_source('sports')
    General_news = get_source('general')
    Technology_news = get_source('technology')

    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,business = Business_news, entertainment = Entertainment_news, sports = Sport_news,  general=General_news, technology=Technology_news)

