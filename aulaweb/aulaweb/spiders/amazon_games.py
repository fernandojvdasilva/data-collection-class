import scrapy
from scrapy import Request

from scrapy import Selector


import pudb; pudb.set_trace()

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_games"
    start_urls=["https://www.amazon.com.br/games"]


    def parse(self, response):
        # Precisamos abrir o arquivo em modo "escrita" para criar o arquivo (ou sobrescrever)
        csv_file = open('amazon_games.csv', 'w')

        # Extraindo todas as divs
        hxs = Selector(response)

        divs = hxs.select('//div[@class="s-item-container"]')

        for i, div in enumerate(divs):
            name = div.select('.//h2/text()').get()
            price = div.select('.//span[contains(@class, "s-price")]/text()').get()
            stars = div.select('.//i[contains(@class, "a-icon-star")]/span/text()').get()

            csv_file.write('%s;%s;%s\n' % (name, price, stars) )

        csv_file.close()

        # Extraindo a URL da próxima página e fazendo uma nova requisição
        next_url = response.xpath('//a[@id="pagnNextLink"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)


    # As páginas seguintes são diferentes, precisamos usar outra função de parser
    def parseNextPage(self, response):

        # Vamos abrir o arquivo em modo "Append", para continuar a escrever nele
        csv_file = open('amazon_games.csv', 'a')

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
            yield response.follow(next_url, callback=self.parseNextPage)
