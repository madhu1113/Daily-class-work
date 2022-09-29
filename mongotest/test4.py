# extraction of data
import pymongo
client = pymongo.MongoClient("mongodb+srv://madhu1311:mongo123@cluster0.zisjox6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["madhu1"]
# write a query to fetch all the data
# record = collection.find()
# for i in record:
#     print(i)

# write a query where companyName is iNeuron
# data = collection.find({"companyName" : "iNeuron"})
# for i in data:
#     print(i)

#  write a query where courseOffered is grater than E
data = collection.find({"courseOffered" : {"$gt": "E"}}) # $ is symbol of inititiation of your query
for i in data:
    print (i)


