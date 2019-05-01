import scrapy

import pudb; pudb.set_trace()

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_games"
    start_urls=["https://www.amazon.com.br/games"]


    def parse(self, response):
        html_file = open('amazon_games.csv', 'w')

        game_names = response.css('h2::text').getall()

        for name in game_names:
            html_file.write(name + '\n')

        html_file.close()