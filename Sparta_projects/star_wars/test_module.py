import unittest
from starships import Starship
from bson.objectid import ObjectId


class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ship1 = Starship(2)
        self.ship2= Starship(5)
        self.ship3 = Starship(10)

    def test_get_info(self):
        actual = self.ship1.get_info()
        expected = {'name': 'CR90 corvette', 'model': 'CR90 corvette', 'manufacturer': 
            'Corellian Engineering Corporation', 'cost_in_credits': '3500000', 'length': '150',
            'max_atmosphering_speed': '950', 'crew': '30-165', 'passengers': '600', 
            'cargo_capacity': '3000000', 'consumables': '1 year', 'hyperdrive_rating': '2.0', 
            'MGLT': '60', 'starship_class': 'corvette', 'pilots': [], 'films': ['https://swapi.dev/api/films/1/',
            'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'], 
            'created': '2014-12-10T14:20:33.369000Z', 'edited': '2014-12-20T21:23:49.867000Z', 
            'url': 'https://swapi.dev/api/starships/2/'}
        self.assertEqual(
            actual, expected,
            "Expected to return JSON object of Starship instance."
        )

    def test_get_pilot_names(self):
        actual = self.ship3.get_pilot_names()
        expected = ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb']
        self.assertEqual(
            actual, expected,
            "Expected to return a list of pilot names from of Starship instance."
        )
        
    def test_get_pilot_ids(self):
        actual = self.ship3.get_pilot_ids()
        expected = [{'_id': ObjectId('6479cb1d0ad3df8e9f5c4f81')}, {'_id': ObjectId('6479cb1e85491def20aaef96')}, 
                    {'_id': ObjectId('6479cb1ed9c7aecbb5523799')}, {'_id': ObjectId('6479cb1eefd47013daba93cb')}]
        self.assertEqual(
            actual, expected,
            "Expected to return a list of dictionaries containing pilot '_ids' from local database."
        )
    
    def test_get_pilot_id(self):
        actual = self.ship3.get_pilot_id("Obi-Wan Kenobi")
        expected = {'_id': ObjectId('6479cb1e4f1b06fb75f98b76')}
        self.assertEqual(
            actual, expected,
        "Expected to return the pilots 'id' from local database matching."
        )   
        
   
if __name__ == "__main__":
    unittest.main()
