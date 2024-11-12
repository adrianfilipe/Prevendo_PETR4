import scrapy



class PetrobrasNewsSpider(scrapy.Spider):
    name = 'petrobras_news'
    # allowed_domains = ['google.com']
    start_urls = [
        'https://www.google.com.br/search?q=petrobras&sca_esv=88f3ba43b8b69cfe&tbs=cdr:1,cd_min:9/1/2024,cd_max:9/30/2024,sbd:1&tbm=nws&sxsrf=ADLYWIKxSodCWd7N3c6AjzB8x4CVZrxk6w:1729618729045&source=lnt&sa=X&ved=2ahUKEwjm6MPvw6KJAxU1r5UCHedKElUQpwV6BAgEEBo&biw=1912&bih=964&dpr=1'
    ]

    # Ponto de entrada para o spider
    def parse(self, response):
        # Seleciona os blocos de artigos de notícias
        articles = response.xpath('//div/text()')

        for article in articles:
            # Captura o título
            title = article.xpath('//div/text()').get()
            
            # # Captura a data da publicação
            # date = article.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "LfVVr", " " ))]/text()').get()
 
            # # Captura a fonte da notícia
            # source = article.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "NUnG9d", " " ))]/text()').get()

            # Gera os dados
            yield {
                'title': title,
                # 'date': date,
                # 'source': source,
            }

        # Paginação: Procura pelo link da próxima página e faz nova requisição
        # next_page = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fl", " " ))]/@href').get()
        # if next_page:
        #     next_page_url = response.urljoin(next_page)
        #     yield scrapy.Request(next_page_url, callback=self.parse)

