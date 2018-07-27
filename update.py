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

def clear():
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db = client['job']
    collection =  db['position']
    data = collection.find({"create_time": {'$regex': '发布于'}})
    for item in data:
        where = {"_id":item['_id']}
        name,work_year,educational = clear_position(item['position_name'])
        create_time = clear_time(item['create_time'])
        salary = clear_salary(item['salary'])
        updates = {
            "create_time":create_time,
            "salary":salary,
            "name":name,
            'work_year':work_year,
            'educational':educational,
            'body':item['body'].lstrip()
        }
        # updates = {
        #     "position_name":item['name']
        # }
        collection.update(where,{"$set":updates})
        print(item['postion_id']+"更新了")
        pass
    client.close()


if __name__ == "__main__":
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db = client['job']
    collection =  db['position']
    group = {
        "$group": {
            "_id": "$create_time",
            "count": {
                "$sum": 1
            }
        }

    }
    alias = {
        '$project': {

            'count': 1,
            "_id": 0,
            "month": "$_id",
        }
    }
    project = {
        "$project": {
            "date": "$_id",
            "count": 1,
            "_id": 0
        }
    }
    sort = {"$sort": {"_id": -1}}
    pipeline = [group,sort,project]

    res = collection.aggregate(pipeline =pipeline)
    for x in res:
        print(x)

    pass

