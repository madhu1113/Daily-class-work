import pymongo
client = pymongo.MongoClient("mongodb+srv://madhu1311:mongo123@cluster0.zisjox6.mongodb.net/?retryWrites=true&w=majority")
db = client.test


data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database = client["inventory"]
collection = database["table"]
#  insert all the data
# collection.insert_many(data)
# d = collection.find()
# for i in d:
#     print(i)

#  find the data where status is A
# d = collection.find({"status" : 'A'})
# for i in d:
#     print(i)

#  status is either A or D
# d = collection.find({"status" : {'$in' :['A', 'P']}})  #whenever you are writing conditions you have to write $
# for i in d:
#     print(i)

#  status shouls be grater than grater than equal to  C
# d = collection.find({"status": {"$gt" : "C"}})
# for i in d:
#     print(i)

#  qty should be grater than 25
# d = collection.find({"qty": {"$gte" : 25}})
# for i in d:
#     print(i)


# find a record where item is sketchpad and qty is 95
# d = collection.find({'item': 'sketch pad', 'qty': 95 })
# for i in d:
#     print(i)


d = collection.find({'item': 'sketch pad', 'qty': {"$gte":75} })
for i in d:
    print(i)


