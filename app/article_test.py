import unittest
from models import article
Article = article.Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Sys-con.com','Cryptohopper Just Hit 100 Platform','Cryptohopper just  platform. In litter…','null','2019-02-15T14:03:04Z','enticed by the promise to invest completely automatically','https://images.pexels.com/photos/417142/pexels-photo-417142.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500','mamie')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
if __name__=='__main__':
    unittest.main()