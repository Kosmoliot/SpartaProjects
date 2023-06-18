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

load_dotenv("/Users/miguel/Desktop/Coding/Sparta/MongoDB/.env")
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
            # # Insert data into the collection
            collection.insert_one(data[0])

# Main class for every ship that we will pull from the API database
# Will take ship number as an argument and will have such instance variables as
# general info, it's own name, list of pilot names and a list of pilot ids.

class Starship():
    def __init__(self, ship_nr) -> None:
        try:
            self.ship_nr = ship_nr
            self.info = self.get_info()
            self.name = self.info['name']
            self.pilot_names = self.get_pilot_names()
            self.pilot_ids = self.get_pilot_ids()
        except ValueError as err_message:       # Using try&except to catch error
            print(err_message)
                
# Will get the general info from SW API and store it as JSON
    def get_info(self):
        sw_api = requests.get(f"https://swapi.dev/api/starships/{self.ship_nr}")
        if sw_api.status_code == requests.codes.ok:
            return sw_api.json()
        else:
            raise ValueError("No ship found in the SW API database.")
    
# Will get the list of pilot urls from instace variable info and use
# request module to pull the pilot's info from SW API and store their
# names in a list which will be returned and stored in instance variable pilot_names
    def get_pilot_names(self):
        pilot_names = []
        for pilot in self.info["pilots"]:
            sw_api = requests.get(pilot)
            if sw_api.status_code == requests.codes.ok:
                pilot_name = requests.get(pilot).json()["name"]
                pilot_names.append(pilot_name)
        return pilot_names


# Using instance variable pilot_names to iterate through the names of pilots
# and find their ids in a local database. Returns another instance variable
# called pilot_ids as a list 
    def get_pilot_ids(self):
        pilot_ids = []
        for name in self.pilot_names:
            pilot_id = self.get_pilot_id(name)
            pilot_ids.append(pilot_id)
        return pilot_ids

# Using parameter name to send a query to local database to find pilot's id
# and return it
    def get_pilot_id(self, name):
        pilot_id = list(db.characters.find({"name": name}, {"id":1}))
        return pilot_id[0]


# Main function which will create Starship class objects for the specified
# range of ship numbers which is passed as an argument. It will check if request
# module response is "ok", create an object, overwrite pilot "url" list with instance
# variable that contains pilot ids and will upload that object to the new collection
# "starships" in local MongoDB "starwars" database.
def main_function(range_nr):
    for i in range(range_nr):
        sw_api = requests.get(f"https://swapi.dev/api/starships/{i}")
        if sw_api.status_code == requests.codes.ok:
            ship = Starship(i)
            ship.info["pilots"] = ship.pilot_ids
            db.starships.insert_one(ship.info)
        
        
main_function(36)

client.close()