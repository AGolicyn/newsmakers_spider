import scrapy
from scrapy.crawler import CrawlerProcess


class RbcSpider(scrapy.Spider):
    name = 'rbc'
    start_urls = ['https://www.rbc.ru/']


    def parse_start_url(self):
        for url in self.start_urls:
            a = scrapy.Request(url,
                               headers={"Cookie": "toprbc_region=world"},
                               cookies=[{'toprbc_region': 'world'}],
                               callback=self.parse,)
            print(a.cb_kwargs)
            yield a

    def parse(self, response, **kwargs):
        hrefs = response.css('.main__big > a::attr(href)').getall()
        [hrefs.append(href) for href in response.css('.main__feed > a::attr(href)').getall()
         if 'from_main' in href
         and 'www.rbc.ru' in href
         and 'spb_sz' not in href]

        yield from response.follow_all(hrefs, self.parse_news_from_main_page)

    def parse_news_from_main_page(self, response):
        text = response.css('.article__text > p *::text').getall()
        text = ''.join(text)
        item = {
            'rbc': text
        }
        yield item
class LentaSpider(scrapy.Spider):

    name = 'lenta'
    start_urls = ['https://lenta.ru/']

    def parse(self, response, **kwargs):
        hrefs = [self.start_urls[0]+href for href in response.css('.last24 > a._compact::attr(href)').getall()]
        yield from response.follow_all(hrefs, self.parse_news_from_main_page)

    def parse_news_from_main_page(self, response):
        text = response.css('.topic-body__content > p *::text').getall()
        text = ''.join(text)
        item = {
            "lenta": text
        }
        yield item
class RiaSpider(scrapy.Spider):
    name = 'ria'
    start_urls = ['https://ria.ru/']

    def parse(self, response, **kwargs):
        hrefs = response.css('.section__content > .floor *::attr(href)').getall()[11:22]
        # print(hrefs)
        yield from response.follow_all(hrefs, self.parse_news_from_main_page)


    def parse_news_from_main_page(self, response):
        text = response.css('.article__text *::text').getall()[1:]
        text = ''.join(text)
        item = {
            'ria': text
        }
        yield item
class KommersantSpider(scrapy.Spider):
    name = 'komm'
    start_urls = ['https://www.kommersant.ru/']

    def parse(self, response, **kwargs):
        hrefs = [self.start_urls[0]+href for href in response.css('.top_news *::attr(href)').getall()[:10]]
        yield from response.follow_all(hrefs, self.parse_news_from_main_page)

    def parse_news_from_main_page(self, response):
        text = response.css('.doc__text *::text').getall()
        text = ''.join(text)
        item = {
            'komm': text
        }
        yield item
class AifSpider(scrapy.Spider):
    name = 'aif'
    start_urls = ['https://aif.ru/']

    def parse(self, response, **kwargs):
        hrefs = response.css('.top5 *::attr(href)').getall()
        hrefs.extend(response.css('.main_top_block *::attr(href)').getall())

        yield from response.follow_all(hrefs, self.parse_news_from_main_page)

    def parse_news_from_main_page(self, response):
        text = response.css('.article_text > p *::text').getall()
        text = ''.join(text)
        item = {
            'aif': text
        }
        yield item


process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "jsonlines"},
    },
    "FEED_EXPORT_ENCODING": 'utf-8',
    "USER_AGENT": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',

})


process.crawl(RbcSpider)
process.crawl(LentaSpider)
process.crawl(RiaSpider)
process.crawl(KommersantSpider)
process.crawl(AifSpider)

process.start()

