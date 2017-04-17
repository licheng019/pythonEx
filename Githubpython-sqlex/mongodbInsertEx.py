from pymongo import MongoClient
conn = MongoClient('localhost')
db = conn.christest
students = db.test.students
students.remove(None)

chris = {
    "name": "chris",
    "age": 30,
    "sex": "M",
    "contact": {
        "email1": "abc@def.com",
        "email2": "def@abc.net"
    }
}
sherry = {
    "name": "sherry",
    "habit": {
        "habit1": "eat",
        "habit2": "sleep"
    },
    "age": 20
}

#insert_one(doc)
students.insert_one(chris)
x = students.insert_one(sherry)

#insert_many(doc,ordered=True/False)
from faker import Factory
import random
def getFakeData(n=10):
    userFaker = Factory.create()
    label = ['name','address','email','age']
    result = []
    for i in range(n):
        x = [userFaker.name(), userFaker.address(), userFaker.email(), random.randint(10,40)]
        result.append(dict(zip(label,x)))
    return result
userinfo = getFakeData()
students.insert_many(userinfo,ordered=False)
