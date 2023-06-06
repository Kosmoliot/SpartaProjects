import requests
import pymongo


# Exercise: The data in this database has been pulled from https://swapi.dev/. 
# As well as 'people', the API has data on starships. In Python, pull data on 
# all available starships from the API. The "pilots" key contains URLs pointing 
# to the characters who pilot the starship. Use these to replace 'pilots' with 
# a list of ObjectIDs from our characters collection, then insert the starships 
# into their own collection. Use functions at the very least!


client = pymongo.MongoClient()
db = client["starwars"]


class Starship():
    def __init__(self, ship_nr) -> None:
        try:
            self.ship_nr = ship_nr
            self.info = get_info(ship_nr)
            self.pilot_names = get_pilot_names(self.info)
            self.pilot_ids = get_pilot_ids(self.pilot_names)
        except ValueError as err_message:
            print(err_message)
                

def get_info(ship_nr):
    sw_api = requests.get(f"https://swapi.dev/api/starships/{ship_nr}")
    if sw_api.status_code == requests.codes.ok:
        return sw_api.json()
    else:
        raise ValueError("No ship found in the SW API database.")
    

def get_pilot_names(stats):
    pilot_names = []
    for pilot in stats["pilots"]:
        sw_api = requests.get(pilot)
        if sw_api.status_code == requests.codes.ok:
            pilot_name = requests.get(pilot).json()["name"]
            pilot_names.append(pilot_name)
    return pilot_names


def get_pilot_ids(pilot_names):
    pilot_ids = []
    for name in pilot_names:
        pilot_id = get_pilot_id(name)
        pilot_ids.append(pilot_id)
    return pilot_ids


def get_pilot_id(name):
    pilot_id = list(db.characters.find({"name": name}, {"id":1}))
    return pilot_id[0]


def main_function():
    for i in range(36):
        sw_api = requests.get(f"https://swapi.dev/api/starships/{i}")
        if sw_api.status_code == requests.codes.ok:
            ship = Starship(i)
            ship.info["pilots"] = ship.pilot_list
            db.starships.insert_one(ship.info)
        
        
# main_function()

