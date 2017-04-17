from pymongo import MongoClient

conn = MongoClient("localhost")
db = conn.christest
students = db.test.students
#replace_one(filter,replacement,upsert=False)
#update_one(filter,update,upsert=True/False), If upsert = True,means insert the data if there is no match one

students.update_many({},{'$inc':{'age':2}})