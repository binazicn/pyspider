import scrapy


class KeQqSpider(scrapy.Spider):
    name = 'ke_qq'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']

    def parse(self, response):
        pass
