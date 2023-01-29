# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        print(spider)
        return item

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
        new_text = ' '.join([title for title in new_text if title and (len(title.split()) > 3)])

        item['data'] = new_text

        return item
