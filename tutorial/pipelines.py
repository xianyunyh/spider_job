# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime
from scrapy.conf import settings

# 学历列表
educations = ("不限","大专","本科","硕士","博士")
#修正学历 有些职位中的学历明显不一致。需要修正
def clean_education(edu,body):
    if edu not in educations:
        for i in educations:
            if i in body:
                edu = i
            else:
                edu = '不限'
    return edu

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

#判断PHP是否在职位名称中，不在就过滤掉。
#jd中含有php不参考，因为很多jd中都乱写
def clean_name(name):
    if "PHP" not in name.upper():
        return False
    return True


class TutorialPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['position2']
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
        item['educational'] = clean_education(item['educational'],item['body'])
        is_php = clean_name(item['position_name'])
        if is_php is True:
            collection.insert(dict(item))
        client.close()
        return item


#处理51job数据
class FiveJobPipeline(object):

    def clear_salary(self,salary):
        lists = salary.split("/")[0].split('-')
        min,max = lists
        unit = 10000
        if "千" in max:
            unit = 1000
            max = max.replace("千","")
        else:
            max = max.replace("万","")
        print(max)
        result = {}
        result['min'] = float(min)*unit
        result['max'] = float(max)*unit
        result['avg'] = (result['max']+result['min'])/2
        return result
    def clear_address(self,address):
        if "上班地址" in address:
            address = address.replace("上班地址 :"," ")
        return address
    def clear_workyear(self,work_year):
        if "经验" in work_year:
           work_year =  work_year.replace("工作经验"," ") or work_year.replace("经验"," ")
        return work_year
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['51job']
        item['salary'] = self.clear_salary(salary=item['salary'])
        item['address'] = self.clear_address(address=item['address'])
        item['work_year'] = self.clear_workyear(work_year=item['work_year'])
        collection.insert(dict(item))
        client.close()
        return item
