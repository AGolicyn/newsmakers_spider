from datetime import datetime
import random
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_splash import SplashRequest

settings = get_project_settings()

class UsaSpider(scrapy.Spider):
    name = 'usa'

    start_urls = settings['US_NEWSPAPERS_URLS']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                errback=self.errback_httpbin,
                headers={
                    'user-agent': random.choice(settings['USER_AGENT_LIST']),
                }
            )

    def parse(self, response, **kwargs):
        text = response.css('body *::text').getall()
        item = {
            "url": response.url,
            "time": datetime.now(),
            "lang": 'EN',
            "data": text
        }
        yield item

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))


process = CrawlerProcess(settings=get_project_settings())
process.crawl(UsaSpider)
process.start()
