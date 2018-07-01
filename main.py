
from message import Message
from scrape import Scrape


def main():

    page = 'https://www.canyon.com/en-us/outlet?--wysiwyg_cany\
on_products-factoryoutlet%5B%40package%5D=wysiwyg.canyon.products&--wysiwyg_cany\
on_products-factoryoutlet%5B%40controller%5D=factoryoutlet&--wysiwyg_canyon_pro\
ducts-factoryoutlet%5B%40action%5D=road&--wysiwyg_canyon_products-factoryoutlet\
%5B%40format%5D=html'

    links = Scrape.scrape(Scrape(), page)

    if links:

        message = Message.format(Message(), links)
        Message.send(Message(), message)

if __name__ == '__main__':

    main()
