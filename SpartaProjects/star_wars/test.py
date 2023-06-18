import requests
import pymongo
from dotenv import load_dotenv
import os
import json

# Exercise: The data in this database has been pulled from https://swapi.dev/. 
# As well as 'people', the API has data on starships. In Python, pull data on 
# all available starships from the API. The "pilots" key contains URLs pointing 
# to the characters who pilot the starship. Use these to replace 'pilots' with 
# a list of ObjectIDs from our characters collection, then insert the starships 
# into their own collection. Use functions at the very least!

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = pymongo.MongoClient(MONGODB_URL)
db = client.starwars

collection = db.characters

# Specify the folder path
folder_path = 'star_wars_files'

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            # Load JSON data from file
            data = json.load(file)
            # Insert data into the collection
            collection.insert_one(data[0])