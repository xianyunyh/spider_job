import jieba               #分词库
import  jieba.analyse
import  pymongo
import redis
import os
import re
import json

client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['job']
collection =  db['position']

data = collection.find({})
text = ""
for item in data:
    text += item['body']
pwd = os.path.split(os.path.realpath(__file__))[0]
stopWord = pwd+'/stop.txt'
jieba.analyse.set_stop_words(stopWord)
cut_text= jieba.cut(text)

it_text = dict({})
for x in cut_text:
    G = re.match('[a-zA-Z]+',x)
    if G:
        key = G.group()
        keys =  map(lambda x: x.lower(), it_text.keys())
        if key.lower() in keys:
            it_text[key.lower()] += 1
        else:
            it_text[key.lower()] = 1
with open("word.json","w+",encoding="utf-8") as file:
    data = file.write(json.dumps((it_text)))


result= "/".join(cut_text)#必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
data = jieba.analyse.extract_tags(result.replace('/',''), withWeight=False, allowPOS=())
#print(",".join(data))
