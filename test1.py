import pymongo
client = pymongo.MongoClient("mongodb+srv://Prashikgole:maruti7609@cluster07.3ohjsfu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client["myinfo"]
collection = database["gole"]


#data = collection.find({"name" : "prashik"})


data = collection.find({"courseOffered" : {"$gt": "E"}})
for i in data:
    print(i)
