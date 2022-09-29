import pymongo

# pip install pymongo
client = pymongo.MongoClient("mongodb+srv://madhu1311:mongo123@madhu.d9pi0x0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
# trying to block my DNS server from my current location so we are getting error hence
# pip install "pymongo[srv]"
d = {
    "name" : "madhu",
    "email" : "madhu.priya@klh.edu.in",
    "surname": "priya"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
#
#
