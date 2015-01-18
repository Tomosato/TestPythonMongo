import pymongo

hostName = "hostnName"
portNumber = portNumber

client = pymongo.MongoClient(hostName,portNumber);

db = client['testPyMongo']

print(db.name)
print(db['testPyMongo'])
