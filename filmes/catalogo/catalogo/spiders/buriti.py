import scrapy


class BuritiSpider(scrapy.Spider):
    name = 'buriti'
    
    start_urls = ['https://buritishopping.com.br/cinema.asp']

    def parse(self, response):
        divs = response.xpath("//*[@id="lazer-cinema"]/div/div[2]/div/div/div[1]/div[2]/div[2]/div")
        for div in divs:
            ingresso = div.xpath('.//a')
            filme = div.xpath('./text()').extract_first()
            href = ingresso.xpath('./@href').extract_firs()
            img = div.xpath('.//img[contains(@alt)]')
