import pymongo
from dotenv import load_dotenv
import os
import pprint

load_dotenv("/Users/miguel/Desktop/Coding/Sparta/MongoDB/.env")
MONGODB_URL = os.environ["MONGODB_URL"]

client = pymongo.MongoClient(MONGODB_URL)
db = client.starwars
collection = db.starships


match = {"$match": {"name": "Millennium Falcon"}}

lookup = {
        "$lookup": {
            'from': db.characters,
            'localField': "pilots._id",
            'foreignField': '_id',
            'as': 'pilotsInfo'
        }
    }
unwind  = {"$unwind": "$pilotsInfo"}
project = {"$project": {"_id": 0, "name": 1, "$pilotsInfo": 1}}

pipeline = [match, lookup, unwind, project]

# result = collection.aggregate(pipeline)


# for doc in result:
#     pprint.pprint(doc)

result = collection.aggregate(pipeline)

print(result)