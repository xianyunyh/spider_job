# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime
class TutorialPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['position']
        collection.insert(dict(item))
        client.close()
        return item

#处理直聘网数据
class ZhipinPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['position']
        now_year = datetime.datetime.now().year
        if '发布于' in  item['create_time']:
            item['create_time'] = item['create_time'].replace("发布于", str(now_year)+"-")
            item['create_time'] = item['create_time'].replace("月", "-")
            item['create_time'] = item['create_time'].replace("日", "")
            if item['create_time'].find("昨天") > 0:
                item['create_time'] = str(datetime.date.today() - datetime.timedelta(days=1))
            elif item['create_time'].find(":") > 0:
                item['create_time'] = str(datetime.date.today())
        collection.insert(dict(item))
        client.close()
        return item
