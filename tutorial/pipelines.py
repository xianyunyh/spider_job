# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime

def clear_salary(salary):
    res = salary.split("-")
    temp = []

    for x in res:
        temp.append(int(x.upper().replace("K"," "))*1000)
    result = {
        "min":temp[0],
        "max":temp[1],
        "avg":int((temp[0]+temp[1])/2)
    }
    return result


def clear_time(time):
    now_year = datetime.datetime.now().year
    if '发布于' in  time:
        time = time.replace("发布于", str(now_year)+"-")
        time = time.replace("月", "-")
        time = time.replace("日", "")
        if time.find("昨天") > 0:
            time = str(datetime.date.today() - datetime.timedelta(days=1))
        elif time.find(":") > 0:
            time = str(datetime.date.today())
    return time

def clear_position(name):
    data =  name.split(" ")

    name = data[0]
    work_year = data[-2]
    educational = data[-1]
    return name,work_year,educational


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
        item['salary'] = clear_salary(item['salary'])
        item['create_time'] = clear_time(item['create_time'])
        [item['position_name'], item['work_year'], item['educational']] = clear_position(item['position_name'])

        collection.insert(dict(item))
        client.close()
        return item
