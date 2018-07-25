import pymongo

client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['job']
item = {
    "id":1,
    "username":"222"
}
collection =  db['position']
collection.insert(item)
