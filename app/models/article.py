class Article:
    '''
   Article class to define Article Objects
    '''

    def __init__(self,id,title,description,imageUrl,url,publishedAt,author,content):
        self.id =id
        self.title = title
        self.description = description
        self.imageUrl = imageUrl
        self.url = url
        self.publishedAt = publishedAt
        self.author = author
        self. content = content