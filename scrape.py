
import re
import requests
from bs4 import BeautifulSoup


def main():

    pass


class Scrape:

    def scrape(self, page):

        response = requests.get(page)
        soup = BeautifulSoup(response.content, 'lxml')
        soup = soup.find_all(class_='teaser-box-wide')
        url = 'https://www.canyon.com'
        links = []

        for hit in soup:

            try:

                hit = str(hit)
                page = re.findall(r'(?<=href=").+(?=">)', hit)[0]
                price = re.findall(r'(?<=data-price=").+?(?=")', hit)[0]
                model = re.findall(r'(?<=<h3>).+?(?=\s<\/h3>)', hit)[0]
                model = model.replace('\xa0', ' ').strip()
                size = re.findall(r'(?<=data-size="\|).+?(?=\|)', hit)[0]

                if size == 'M':

                    links.append([model, size, price, url + page])

            except Exception as e:

                pass

        if len(links) != 0:

            return links

        else:

            return links


if __name__ == '__main__':

    main()
