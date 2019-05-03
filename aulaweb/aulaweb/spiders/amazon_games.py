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
        game_names = response.xpath('//div[@class="s-item-container"]//h2/text()').getall()
        game_prices = response.xpath('//div[@class="s-item-container"]//span[contains(@class, "s-price")]/text()').getall()
        game_platforms = response.xpath('//div[@class="s-item-container"]//h3/text()').getall()

        len(game_names)
        len(game_prices)
        len(game_platforms)

        for name, price, plat in zip(game_names, game_prices, game_platforms):
            # Ignorando quando não houver plataforma
            if plat in ['Branco', 'Preto']:
                plat = ''
            csv_file.write('%s;%s;%s\n' % (name, price, plat) )

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
        game_prices = response.xpath('//div[@class="sg-row"]//span[contains(@class, "a-price")]/span[@class="a-offscreen"]/text()').getall()
        game_platforms = response.xpath('//div[@class="sg-row"]//div[contains(@class,"a-section")]//a[contains(@class, "a-link-normal a-text-bold")]/text()').getall()

        print(len(game_names))
        print(len(game_prices))
        print(len(game_platforms))

        for name, price, plat in zip(game_names, game_prices, game_platforms):
            plat = plat.replace('\n', '')
            plat = plat.replace(' ', '')
            plat = plat.replace('\t', '')
            csv_file.write('%s;%s;%s\n' % (name, price, plat))

        csv_file.close()

        # Extraindo a url da próxima página
        next_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)
        #    next_url = response.urljoin(next_url)
        #    yield scrapy.Request(next_url, callback=self.parseNextPage)