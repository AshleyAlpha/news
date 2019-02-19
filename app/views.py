from flask import render_template
from app import app
from .request import get_source, get_article

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general_category= get_source('general')
    sport_category= get_source('sports')
    business_category = get_source('business')
    entertainement_category = get_source('entertainment')
    technology_category = get_source('technology')
    message = 'Welcome to our news highlight website'
    title = 'NEWS'
# Getting popular news
    return render_template('index.html', title = title, general = general_category, sports = sport_category, business =  business_category, entertainment = entertainement_category,technology =  technology_category  )

# @app.route('/source/<source_name>')
# def source(source_name):
#     '''
#     view source page function that returns the nsource details page and its data.
#     '''
#     return render_template('source.html',id=source_name)

@app.route('/article/<id>')
def article(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    title = id

    return render_template('article.html', title = title, article = article)