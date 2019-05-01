import scrapy

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_games"
    start_urls=["https://www.amazon.com.br/games"]


    def parse(self, response):
        html_file = open('amazon_games.html', 'w')

        html_file.write(str(response.body))

        html_file.close()