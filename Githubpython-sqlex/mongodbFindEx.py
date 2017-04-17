from pymongo import MongoClient
import json
from bson import json_util

conn = MongoClient("localhost")
db = conn.christest
students = db.test.students
#cursor = students.find()
#cursor = students.find({'name':'Misty Yates'})
# cursor = students.find({'name':{'$in':['Misty Yates','Laura Logan']}})
#cursor = students.find({'age':{'$gt':25}})
cursor = students.find({'$or':[{'name':{'$in':['Misty Yates','Laura Logan']}},{'age':{'$gt':30}}]})
# cursor = students.find({'habit.habit1':'eat'})
for student in cursor:
    print student
    print json.dumps(student, indent = 4,default=json_util.default)