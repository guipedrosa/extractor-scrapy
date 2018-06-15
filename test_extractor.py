import unittest

from extractor import Extractor

class TestExtractor(unittest.TestCase):

    def test_extractor_url_access(self):
        print('Test Extractor URL Access construct')
        ex = Extractor('https://google.com')
        
        self.assertRaises(Exception, ex)
        self.assertEqual(ex.soup.title.text, 'Google')

    def test_open_url(self):
        print('Test Extractor opening URL method')

        ex = Extractor()            
        site = ex.open_url('https://google.com')
        
        self.assertRaises(Exception, ex)
        self.assertEqual(site.title.text, 'Google')

    def test_create_csv(self):
        ex = Extractor()                    
        products = [{'nome':'product_test','title':'title_test', 'url': 'http://test.com'}]
        csv = ex.write_csv(products, 'test.csv')
        
        self.assertTrue(csv)



if __name__ == '__main__':
    unittest.main()