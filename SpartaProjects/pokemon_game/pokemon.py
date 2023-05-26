from tabulate import tabulate
from urllib.error import HTTPError
import requests
import random


class Pokemon():
    def __init__(self, pok_name) -> None:
        self.pok_name = pok_name
        self.full_info = get_resource(pok_name)
        self.moves = get_moves(self.full_info)
        self.stats = get_stats(self.full_info)


def get_resource(name):
    pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if pokemon_api.status_code == requests.codes.ok:
        return pokemon_api.json()
    else:
        print("There's no such pokemon, please try again.")


def get_moves(info):
    move_list = {}
    for move in info["moves"]:
        move_list[move["move"]["name"]] = get_move_dmg(move["move"]["url"])
        if len(move_list) == 5:
            break
    return move_list


def get_move_dmg(url):
    pokemon_api = requests.get(url)
    if pokemon_api.status_code == requests.codes.ok:
        return pokemon_api.json()["power"]
    else:
        print("There's no such pokemon, please try again.")
    

def get_stats(info):
    stats = {}
    for stat in info["stats"]:
        stats[stat["stat"]["name"]] = stat["base_stat"]
    return stats


def print_info(pokemon, info, stat, value):
    print(f"\n#========== {pokemon.pok_name.capitalize()} {stat} ==========#")
    table = tabulate([(key, value) for key, value in info.items()], headers=[stat, value], tablefmt="psql")
    print(f"{table}\n")
    

def print_stats(pokemon):
    return print_info(pokemon, pokemon.stats, "Stat", "Value")


def print_moves(pokemon):
   return print_info(pokemon, pokemon.moves, "Moves", "Damage")


def enter_pokemon():
    usr_input = input("Please type in your pokemon name: ")
    if requests.get(f"https://pokeapi.co/api/v2/pokemon/{usr_input}").status_code == requests.codes.ok:
        return Pokemon(usr_input)
    else:
        print("There's no such pokemon, please try again.")


def random_pokemon():
    pokemon_list = ["ditto", "kakuna", "pidgey", "snorlax", "piplup"]
    return Pokemon(random.choice(pokemon_list))
    


def attack(pokemon, opponent, user_attack):
    y_move = list(pokemon.moves.keys())[user_attack-1]
    opponent.stats["hp"] -= pokemon.moves[y_move]
    print(f"\nYou have dealt {pokemon.moves[y_move]} damage")
    o_move = random.choice(list(opponent.moves.values()))
    pokemon.stats["hp"] -= o_move
    print(f"You have received {o_move}")

    
#===============Fight Menu===============#

def fight_menu(pokemon, opponent):
    while True:
        if pokemon.stats["hp"] <= 0:
            print("\nYou won, well done!")
            break
        elif opponent.stats["hp"] <= 0:
            print("\nYou lost, don't be upset. Try again!")
            break
        try:
            user_choice = int(input(f"""\nChoose an attack from the table :
1\t-\t{list(pokemon.moves.keys())[0]}
2\t-\t{list(pokemon.moves.keys())[1]}
3\t-\t{list(pokemon.moves.keys())[2]}
4\t-\t{list(pokemon.moves.keys())[3]}
5\t-\t{list(pokemon.moves.keys())[4]}
\n0\t-\tGive up
: """))
            if user_choice == 1:
                attack(pokemon, opponent, 1)
                
            elif user_choice == 2:
                attack(pokemon, opponent, 2)
            
            elif user_choice == 3:
                attack(pokemon, opponent, 3)
                
            elif user_choice == 4:
                attack(pokemon, opponent, 4)
                
            elif user_choice == 5:
                attack(pokemon, opponent, 5)
            
            elif user_choice == 0:
                print("\nI thought I tought you better!")
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
                return enter_pokemon()
                
            elif user_choice == 2:
                return random_pokemon()
            
            elif user_choice == 0:
                print("\nI thought I tought you better!")
                break
            else:
                print("\nOops - incorrect input")
        except ValueError:
            print("\nEntry should be a number from the menu options.\n")

#===============Main Menu===============#

def main_menu(pokemon):
    while True:
        try:

            user_choice = int(input("""\nWhat would you like to do:
1\t-\tView stats
2\t-\tPrint moves
3\t-\tAttack
0\t-\tRun away
: """))
            if user_choice == 1:
                print_stats(pokemon)  
                
            elif user_choice == 2:
                print_moves(pokemon)
                
            elif user_choice == 3:
                fight_menu(pokemon, random_pokemon())
            
            elif user_choice == 0:
                print("\nCome back you COWARD!")
                break
            else:
                print("\nOops - incorrect input")
        except ValueError:
            print("\nEntry should be a number from the menu options.\n")


main_menu(choose_pokemon())
