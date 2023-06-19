import pymongo
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = pymongo.MongoClient(MONGODB_URL)
db = client.starwars
collection = db.starships


match = {"$match": {"name": "Millennium Falcon"}}

# Takes ObjectID from pilots field in "starships" collection 
# and ooks for matching ObjectID from the "characters" collection.
lookup = {
        "$lookup": {
            'from': "characters",
            'localField': "pilots._id",
            'foreignField': '_id',
            'as': 'pilotsInfo'
        }
    }

# It transforms an array field into multiple documents, each containing a 
# single element from the original array.
unwind  = {"$unwind": "$pilotsInfo"}

# Returns only specified fields with value of "1".
project = {"$project": {"_id": 0, "name": 1, "pilotsInfo.name": 1}}

# Aggregation pipeline
pipeline = [match, lookup, unwind, project]

result = collection.aggregate(pipeline)

for doc in result:
    pprint.pprint(doc)