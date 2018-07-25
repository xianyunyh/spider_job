# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
class TutorialPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['position']
        collection.insert(dict(item))
        client.close()
        return item
