from pymongo import MongoClient

client = MongoClient("mongodb://host:port_number/")
db = client["database"]

cust_collection = db["Customers"]
query = {"key": "value"}
doc = cust_collection.find(query)

for presence in doc:
    print(presence)
