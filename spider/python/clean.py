#！/bin/python
import pymongo
import re
"""
清理数据
"""


client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['job']
collection = db['position']
#学历列表
educations = ("不限","大专","本科","硕士","博士")

# 修正抓取的学历
# 如果没有在列表中，就是不限，如果jd中含有学历要求，以jd为准
def clean_education(education,body):
    if education not in educations:
        education = "不限"
    else:
        for item in educations:
            if item in body:
                education = item
    return education

"""
清理脏数据
如果标题中不含有PHP，或者内容不含有PHP 删掉记录
"""
def clean_data():
    where = {"position_name":{"$not":re.compile("php",re.I)}}
    data = collection.find(where)
    return data

if __name__ == '__main__':
    data = clean_data()
    for x in data:
       if "PHP" not in (x['position_name']).upper():
            #collection.delete_one({"_id":x['_id']})
            print(x['position_name'])
