# mongoDB:- Store document(Dictionary, json based data) based data
# complex query in terms of mysql(complex data modeling) but here no such complexity
# scalability:- mysql(scale it vertically(dedicated server)), mongoDB(scale it horizonally i.e distributed database)
# example:- sqldatabase(mysql, mssql, posgresql, oracle, DB2, MariaDB etc,), NoSQL(MongoDB, Cassandra, Azure Cosmos DB, Amazon DynamoDB, Oracle NoSQL Database,)
# in legeacy system we are using mysql but now a days systems are using mongoDB
import pymongo

client = pymongo.MongoClient("mongodb+srv://madhu1311:mongo123@cluster0.zisjox6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "madhu",
    "mail_id" : "madhu.priya@klh.edu.in",
    "subject" : ["python" , "mongoDB " , "Database "]
} # in technical term document
# collection:- table inside the database(bunch of document)

database = client['myinfo'] # creating databases
collection = database["madhu1"] # creating tables(collection)
collection.insert_one(data) # inside collection we are inserting our data