import scrapy
from scrapy import Request

import pudb; pudb.set_trace()

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_games"
    start_urls=["https://www.amazon.com.br/games"]


    def parse(self, response):
        # Precisamos abrir o arquivo em modo "escrita" para criar o arquivo (ou sobrescrever)
        csv_file = open('amazon_games.csv', 'w')

        # Extraindo o nome dos jogos e salvando no arquivo CSV
        game_names = response.css('h2::text').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        # Extraindo a URL da próxima página e fazendo uma nova requisição
        next_url = response.xpath('//a[@id="pagnNextLink"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)
            #next_url = response.urljoin(next_url)
            #yield scrapy.Request(next_url, callback=self.parseNextPage)

    # As páginas seguintes são diferentes, precisamos usar outra função de parser
    def parseNextPage(self, response):

        # Vamos abrir o arquivo em modo "Append", para continuar a escrever nele
        csv_file = open('amazon_games.csv', 'a')

        # Extraímos os nomes de jogos
        game_names = response.xpath('//span[contains(@class,"a-text-normal")]/text()').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        # Extraindo a url da próxima página
        next_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)
        #    next_url = response.urljoin(next_url)
        #    yield scrapy.Request(next_url, callback=self.parseNextPage)