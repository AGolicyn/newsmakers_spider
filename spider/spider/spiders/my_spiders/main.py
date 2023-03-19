import os
import random
from datetime import datetime

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_splash import SplashRequest
from utils import LANGUAGE_MAPPER, GLOBAL_URLS, COUNTRY_MAPPER

settings = get_project_settings()


class RuSpider(scrapy.Spider):
    name = 'ru'
    start_urls = GLOBAL_URLS

    # start_urls = settings['RU_NEWSPAPERS_URLS']

    def start_requests(self):
        for url in self.start_urls:
            usr_ag = random.choice(settings['USER_AGENT_LIST'])
            yield SplashRequest(
                url=url,
                callback=self.parse,
                errback=self.errback_httpbin,
                headers={
                    'user-agent': usr_ag
                },
                splash_headers={
                    'user-agent': usr_ag,
                },
                args={
                    'wait': 0.5,
                }
            )

    def parse(self, response, **kwargs):
        try:
            result = [
                (value.css('*::text').get(),
                 value.css('::attr(href)').get())
                for value in response.css('a')
            ]
        except TypeError as e:
            self.logger.error(repr(e))
        else:
            for title, href in result:
                # print(result)
                item = {
                    "url": response.url,
                    "href": href,
                    "time": datetime.now(),
                    "lang": LANGUAGE_MAPPER.get(response.url),
                    "country": COUNTRY_MAPPER.get(response.url),
                    "title": title
                }
                yield item

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))


process = CrawlerProcess(settings=settings)
if int(os.environ.get("CRAWL")):
    process.crawl(RuSpider)
    process.start()
