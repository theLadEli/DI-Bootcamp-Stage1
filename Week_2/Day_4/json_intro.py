import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = 'family.json'
json_my_family = json.dump(my_family)

with open(json_file, 'w') as f:
    json.dump(my_family, f)