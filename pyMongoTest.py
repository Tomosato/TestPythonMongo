import pymongo


hostName = "192.168.56.11"
portNumber = 27017
client = pymongo.MongoClient(hostName, portNumber)

db = client.testPyMongo

print(db.name)

print(db.testPyMongo)
