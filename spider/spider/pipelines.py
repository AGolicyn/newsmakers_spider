import os

import zmq
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

settings = get_project_settings()


class TextPipeLine:
    def process_item(self, item, spider):
        # check valid href
        if item['href'] and item['href'].startswith('/'):
            item['href'] = item['url'] + item['href'][1:]

        # drop empty titles
        if not item['title']:
            raise DropItem(r'Empty title found')

        # clear text in titles
        item['title'] = item['title'].strip('\n\t«» ')

        # drop empty or few informative titles
        if not item['title'] or (len(item['title'].split()) < 5):
            raise DropItem(r'Useless title found')

        return item


class PublisherPipeLine:
    def open_spider(self, spider):
        self.context = zmq.Context()

        # Socket to talk to clients
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.sndhwm = 110000
        self.publisher.bind(os.environ.get('SPIDER_PUBLISHER_ADDRESS'))

        # Socket to send signals
        self.syncclient = self.context.socket(zmq.REQ)
        self.syncclient.connect(os.environ.get('SYNCSERVER_ADDRESS'))
        spider.logger.debug(f'Spider start sending sync requests '
                            f'to {os.environ.get("SYNCSERVER_ADDRESS")}')

        self.subscribers = 0
        while self.subscribers < settings['SUBSCRIBERS_EXPECTED']:
            self.syncclient.send(b'')
            self.syncclient.recv()
            self.subscribers += 1

            spider.logger.debug(f'Subscribers {self.subscribers}/1')
        spider.logger.info('All subscribers are present')

    def process_item(self, item, spider):
        spider.logger.debug(f'Sending item {item["url"]}')
        self.publisher.send_json(item, ensure_ascii=False, default=str)
        return item

    def close_spider(self, spider):
        # Send "END" to close subscriber's socket
        self.publisher.send_json({'END': True})
        self.publisher.close()


class DuplicatesPipeLine:
    def __init__(self):
        self.seen_href = set()

    def process_item(self, item, spider):
        if item["href"] in self.seen_href:
            raise DropItem(f'Duplicate item with href {item["href"]}')
        else:
            self.seen_href.add(item["href"])
        return item
