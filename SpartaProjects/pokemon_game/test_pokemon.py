import unittest
from pokemon import Pokemon


class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pok1 = Pokemon("pikachu")
        self.pok2 = Pokemon("mew")
        self.pok3 = Pokemon("bulbasaur")

    def test_get_resource(self):
        result = self.pok1.full_info
        self.assertIsInstance(result, dict, 
        "Expected `get_resource` method to create a dictionary in Pokemon instance variable."
        )
        
    def test_get_moves(self):
        actual = self.pok2.moves
        expected = {'pound': 40, 'mega-punch': 80, 'pay-day': 40, 
        'fire-punch': 75, 'ice-punch': 75}
        self.assertEqual(
            actual, expected,
            "Expected `get_moves` method to create a list of 5 or less moves in instance variable."
        )
        
    def test_get_stats(self):
        actual = self.pok3.stats
        expected = {'hp': 45, 'attack': 49, 'defense': 49, 'special-attack': 65,
        'special-defense': 65, 'speed': 45}
        self.assertEqual(
            actual, expected,
            "Expected `get_stats` method to create a list of stats in instance variable."
        )

if __name__ == "__main__":
    unittest.main()
