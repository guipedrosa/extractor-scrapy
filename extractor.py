from bs4 import BeautifulSoup
import requests
import csv


class Extractor:
    """ Class to implement default extract behavior """

    def __init__(self, url=None):
        
        if url:
            try:
                self.source = requests.get(url).text
            except:
                raise Exception('Site unreachable, verify the URL.')

            self.soup = BeautifulSoup(self.source, 'lxml')   


    def open_url(self, url):
        """ Method to open URLs """
        try:
            source_url = requests.get(url).text
        except:
            raise Exception('Site unreachable, verify the URL.')

        return BeautifulSoup(source_url, 'lxml')


    def write_csv(self, data, file_name='results.csv'):
        """ Write CSV file with scrap's result """

        if len(data) > 0:
            try:
                csv_file = open(file_name, 'w')        
            except:
                raise Exception('Problems to create the CSV file!')

            csv_writer = csv.writer(csv_file)
            
            header = data[0].keys()
            csv_writer.writerow(header)
            seen = set()
            for line in data:
                if line.values() in seen: continue #skip duplicated 
                
                seen.add(line.values())
                csv_writer.writerow(line.values())

            csv_file.close()     

            return True

        return False

if __name__ == '__main__':
    print('Extractor Class')