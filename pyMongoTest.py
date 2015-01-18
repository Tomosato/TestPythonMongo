import pymongo

client = pymongo.MongoClient("192.168.56.11", 27017)

db = client.testPyMongo

print(db.name)

print(db.testPyMongo)
