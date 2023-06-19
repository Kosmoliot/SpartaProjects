import pymongo
from dotenv import load_dotenv
import os
import pprint

load_dotenv("/Users/miguel/Desktop/Coding/Sparta/MongoDB/.env")
MONGODB_URL = os.environ["MONGODB_URL"]

client = pymongo.MongoClient(MONGODB_URL)
db = client.starwars
collection = db.starships


match = {"$match": {"name": "TIE Advanced x1"}}

lookup = {
        "$lookup": {
            'from': "characters",
            'localField': "pilots._id",
            'foreignField': '_id',
            'as': 'pilotsInfo'
        }
    }

unwind  = {"$unwind": "$pilotsInfo"}

project = {"$project": {"_id": 0, "name": 1, "pilotsInfo.name": 1}}

pipeline = [match, lookup, unwind]

result = collection.aggregate(pipeline)

for doc in result:
    pprint.pprint(doc)