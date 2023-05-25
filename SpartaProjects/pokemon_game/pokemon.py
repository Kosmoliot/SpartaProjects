import json
import requests
import random
from tabulate import tabulate




class Pokemon():
    def __init__(self, pok_name) -> None:
        self.pok_name = pok_name
        self.full_info = get_resource(pok_name)


def get_resource(name): 
    pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    return pokemon_api.json()


def get_moves():
    move_list = {}
    with open("pokemon.json") as jsonfile:
        pok_data = json.load(jsonfile)
    for key in pok_data.keys():
        move_list[key] = []
        for move in pok_data[key]["moves"]:
            move_list[key].append(move["move"]["name"])
    return move_list


def get_stats():
    stats = {}
    with open("pokemon.json") as jsonfile:
        pok_data = json.load(jsonfile)
    for key in pok_data.keys():
        stats[key] = []
        for stat in pok_data[key]["stats"]:
            stats[key].append({stat["stat"]["name"]: stat["base_stat"]})
    return stats


def create_combatants(combatant1, combatant2):
    combatants = {combatant1: Pokemon(combatant1).full_info, combatant2: Pokemon(combatant2).full_info}
    with open("pokemon.json", "w") as file:
        json.dump(combatants, file)
        

def print_stats():
    # Convert dictionary to a tuples
    pok_stats = get_stats()
    for pokemon in pok_stats:
        print(f"\n#========== {pokemon.capitalize()} stats ==========#")
        table = tabulate([(k, v) for d in pok_stats[pokemon] for k, v in d.items()], headers=["Key", "Value"], tablefmt="psql")
        print(f"{table}\n")
  

def enter_pokemon():
    usr_input = input("Please type in your pokemon name: ")
    if requests.get(f"https://pokeapi.co/api/v2/pokemon/{usr_input}").status_code == requests.codes.ok:
        return usr_input
    else:
        print("There's no such pokemon, please try again.")


def random_pokemon():
    pokemon_list = ["ditto", "kakuna", "pidgey", "snorlax", "piplup"]
    return random.choice(pokemon_list)


def attack():
    pass


def super_attack():
    pass


def defense():
    pass


def super_defense():
    pass

    
#===============Fight Menu===============#

def fight_menu():
    while True:
        try:

            user_choice = int(input("""\nWhat would you like to do:
1\t-\tView stats
0\t-\tRun away
: """))
            if user_choice == 1:
                print_stats()             
            
            elif user_choice == 0:
                print("\nCome back you COWARD!")
                break
            else:
                print("\nOops - incorrect input")
        except ValueError:
            print("\nEntry should be a number from the menu options.\n")


#===============Choose pokemon===============#
def choose_pokemon():
    while True:
        try:
            user_choice = int(input("""\nWould you like to choose your pokemon or get randomly assigned:
1\t-\tType in your pokemon
2\t-\tGet randomly assigned
0\t-\tGive up
: """))
            if user_choice == 1:
                user_pokemon =  enter_pokemon()
                create_combatants(user_pokemon, random_pokemon())
                fight_menu()
                break
                
            elif user_choice == 2:
                create_combatants(user_pokemon, random_pokemon())
                fight_menu()
                break
            
            elif user_choice == 0:
                print("\nI thought I tought you better!")
                break
            else:
                print("\nOops - incorrect input")
        except ValueError:
            print("\nEntry should be a number from the menu options.\n")

#===============Main Menu===============#


choose_pokemon()