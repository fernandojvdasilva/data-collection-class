import scrapy
from scrapy import Request
from w3lib.url import add_or_replace_parameters

from scrapy import Selector


import pudb; pudb.set_trace()

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_search"

    def start_requests(self):

        first_url = 'https://www.amazon.com.br/s'

        pars = {
            'k': 'fifa',
            'i': 'videogames'
        }

        yield Request(add_or_replace_parameters(first_url, pars), callback=self.parse)


    def parse(self, response):

        # Vamos abrir o arquivo em modo "Append", para continuar a escrever nele
        csv_file = open('amazon_search.csv', 'a')

        # Extraindo todas as divs
        hxs = Selector(response)

        divs = hxs.select('//div[@class="sg-row"]')

        for i, div in enumerate(divs):
            name = div.select('.//span[contains(@class,"a-text-normal")]/text()').get()
            price = div.select('.//span[contains(@class, "a-price")]/span[@class="a-offscreen"]/text()').get()
            stars = div.select('.//i[contains(@class, "a-icon-star-small")]/span/text()').get()

            csv_file.write('%s;%s;%s\n' % (name, price, stars))

        csv_file.close()

        # Extraindo a url da próxima página
        next_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parse)
