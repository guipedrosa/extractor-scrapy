from extractor import Extractor

class EpocaCosmeticos(Extractor):
    """ Specific class to extract data from defined website """

    def __init__(self, url):
        super(EpocaCosmeticos, self).__init__(url)
        
        self.products = []
        menu_categories = self.soup.find_all('a', class_='submenu__list--link')

        # for DEMO, the number of categories are limited
        for item in menu_categories[:2]:
            if item['href'].startswith('https'):
                
                source_product_list = self.open_url(item['href'])
                products_div = source_product_list.find_all('div', class_='shelf-default__item')                
                
                for prod_div in products_div:
                    self.extract_product(prod_div)

        if len(self.products) > 0:
            if self.write_csv(self.products):
                print('CSV File saved!')

    def extract_product(self, prod_div):
        prod = prod_div.find('a', itemprop='name')

        new_product = {}
        new_product['name'] = prod.text
        new_product['titulo'] = self.open_url(prod['href']).title.text
        new_product['url'] = prod['href']
        
        self.products.append(new_product)
        

if __name__ == '__main__':
    print('Executing crawler for Epoca Cosmeticos...')
    crawler_epoca_cosm = EpocaCosmeticos('https://www.epocacosmeticos.com.br/')
    print('Finished')
    # cr1 = Extractor('https://www.epocacosmeticos.com.br/')