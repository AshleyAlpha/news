from app import app
import urllib.request,json
from .models import source
from .models import article
Source = source.Source
Article = article.Article

# getting api key
api_key = app.config['NEWS_API_KEY']
# getting the news base url

base_url = app.config['SOURCE_API_BASE_URL']
articles_base_url=app.config['NEWS_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = get_source_response
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_result(source_results_list)
    return source_results
def process_result(source_list):
    '''
    Function that processes the article result and transform them to a list of objects
    
    Args:
       article_list: A list of dictionaries that contain article details
    Returns:
       article_results:A list of objects
    '''
    source_results =[]
    for source_item in source_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        country = source_item.get('country')
        if source:
            source_object = Source(id,name,description, country)
            source_results.append(source_object)
    return source_results

def get_article(id):
    get_article_details_url = articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        article_object = None
        
        if article_details_response['articles']:
                article_results_list=article_details_response['articles']
                article_results=process_article(article_results_list)
    return article_results
def process_article(article_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
    article_list: A list of dictionaries that contain news details
    Returns :
    news_results: A list of articles objects
    '''
    article_results=[]
    for article in article_list:
        id=article.get('id')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        imageUrl=article.get('urlToImage')
        publishedAt=article.get("publishedAt")
        author=article.get("author")
        content=article.get('content')

        if imageUrl:
            article_object=Article(id,title,description,imageUrl,url,publishedAt,author,content)
            article_results.append(article_object)
    return article_results 
