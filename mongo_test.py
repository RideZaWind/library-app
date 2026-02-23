
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://adrian2718:iGcAvdsbzxhhW7VE@library-db.njhmomj.mongodb.net/?appName=library-db"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["library"]
collection = db["books"]

# collection.insert_one({
#         "name": "Advanced Python",
#         "description": "An advanced Python book explores high-level topics such as "+
#         "object-oriented design, concurrency, performance optimization, metaprogramming,"+
#         "and best practices for building scalable, production-ready applications."
#     })

for f in collection.find():
    print(f["name"])