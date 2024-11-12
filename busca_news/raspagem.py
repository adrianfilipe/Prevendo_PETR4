import scrapy
from datetime import datetime

class PetrobrasNewsSpider(scrapy.Spider):
    name = 'petrobras_news'
    allowed_domains = ['news.google.com']
    start_urls = [
        'https://news.google.com/search?q=petrobras%20after%3A2022-01-01%20before%3A2023-12-31'
    ]

    def parse(self, response):
        # Seleciona todos os blocos de notícias
        articles = response.xpath('//div[@class="xrnccd"]')

        for article in articles:
            title = article.xpath('.//h3/a/text()').get()
            link = article.xpath('.//h3/a/@href').get()

            date = article.xpath('.//time/@datetime').get()

            # Tratamento do link
            if link:
                link = response.urljoin(link)

            # Se a data estiver no formato correto, converte para datetime
            if date:
                date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

            yield {
                'title': title,
                'link': link,
                'date': date,
            }

        # Paginação: Procura pelo link para a próxima página e faz nova requisição
        next_page = response.xpath('//a[@class="nBDE1b G5eFlf"]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
