import json

import zmq
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class TextPipeLine:
    def process_item(self, item, spider):

        text = [text.strip(' \n\t') for text in item['data']]
        new_text = []

        for sentence in text:
            for char in sentence:
                if char in '%{}[]<>;/=-*+()|':
                    break
            else:
                new_text.append(sentence)
        new_text = '. '.join([title for title in new_text if title and (len(title.split()) > 3)])

        item['data'] = new_text

        return item

class PublisherPipeLine:
    def open_spider(self, spider):
        print('OPEN SPIDER')
        self.context = zmq.Context()

        # Socket to talk to clients
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.sndhwm = 110000
        self.publisher.bind("tcp://*:5561")

        # Socket to receive signals
        self.syncservice = self.context.socket(zmq.REP)
        self.syncservice.bind("tcp://*:5562")

        self.subscribers = 0
        while self.subscribers < settings['SUBSCRIBERS_EXPECTED']:
            msg = self.syncservice.recv()
            self.syncservice.send(b'')
            self.subscribers += 1

            spider.logger.debug(f'Subscribers {self.subscribers}/2')
        spider.logger.info('All subscribers are present')

    def process_item(self, item, spider):
        spider.logger.debug(f'Sending item {item["url"]}')
        self.publisher.send_json(json.dumps(item, ensure_ascii=False, default=str))
        return item

    def close_spider(self, spider):
        self.syncservice.close()
        self.publisher.close()