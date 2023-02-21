import json

import zmq
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class TextPipeLine:
    def process_item(self, item, spider):
        # check valid href
        if item['href'] and item['href'].startswith('/'):
            item['href'] = item['url'] + item['href'][1:]

        # check text informative
        title = item['title']
        if title:
            item['title'] = title.strip('\n\t«» ')
        if title and len(title.split()) < 5:
            item['title'] = ''

        return item


class PublisherPipeLine:
    def open_spider(self, spider):
        self.context = zmq.Context()

        # Socket to talk to clients
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.sndhwm = 110000
        self.publisher.bind("tcp://*:5561")

        # Socket to send signals
        spider.logger.debug('Wait for subscribers...')
        self.syncclient = self.context.socket(zmq.REQ)
        self.syncclient.connect(settings['SYNCSERVER_ADDRESS_1'])
        # self.syncclient.connect(settings['SYNCSERVER_ADDRESS_2'])

        self.subscribers = 0
        while self.subscribers < settings['SUBSCRIBERS_EXPECTED']:
            self.syncclient.send(b'')
            msg = self.syncclient.recv()
            self.subscribers += 1

            spider.logger.debug(f'Subscribers {self.subscribers}/2')
        spider.logger.info('All subscribers are present')

    def process_item(self, item, spider):
        if item['title']:
            spider.logger.debug(f'Sending item {item["url"]}')
            self.publisher.send_json(item, ensure_ascii=False, default=str)
        return item

    def close_spider(self, spider):
        # Send empty to close subscriber's socket
        self.publisher.send_json({'END': True})
        self.publisher.close()
