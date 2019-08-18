import  redis
import pymongo
if __name__ == '__main__':
    pool= redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
    r=redis.Redis(connection_pool=pool)
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db = client['job']
    collection =  db['position']
    data = collection.find({})
    for item in data:
        r.sadd("positionIds",item['postion_id'])
        print(item['postion_id']+"添加成功")
    pass
