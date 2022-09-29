import pymongo
client = pymongo.MongoClient("mongodb+srv://madhu1311:mongo123@cluster0.zisjox6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
] # this is called json
database = client['myinfo'] # creating databases
collection = database["madhu1"]
collection.insert_many(list_of_records)
