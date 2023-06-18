import json

my_dict = {"name": "Michail", "surname": "Pliuscik", "age": 37, "height": 168}

# print(type(my_dict))
# print(my_dict)

dict_json_str = json.dumps(my_dict)
# print(dict_json_str)
# print(type(dict_json_str))

# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(my_dict, jsonfile)
    
with open("new_json_file.json") as jsonfile:
    my_data = json.load(jsonfile)
    print(my_data)
    print(type(my_data))

# data = json.loads(dict_json_str)
# print(type(data))