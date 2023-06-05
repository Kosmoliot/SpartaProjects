from starships import Starship
from unittest import main


ship = Starship(10)
print(ship.name)
print(ship.pilot_names)
print(ship.pilot_ids)


# Run unit tests automatically
main(module='test_module', exit=False)