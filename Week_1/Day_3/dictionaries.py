# user_info = {
#     'name': 'Eli',
#     'age': 18,
#     'location': 'Tel Aviv',
#     'pets': ['Toothless', 'Luli', 'Maple'],
#     'family': {
#         'name': 'Avi',
#         'age': 10,
#         'relation': 'brother'
#     }
# }

# print(user_info['family']['age'])

sample_dict = { 
    'name': 'Eli',
    'age': 18,
    'location': 'Tel Aviv',
    'pets': ['Toothless', 'Luli', 'Maple'],
    'family': {
        'name': 'Avi',
        'age': 10,
        'relation': 'brother'
    }
}

# for value in sample_dict.values():
#     print(f'The value is: {value}')

# for key in sample_dict.keys():
#     print(f'The key is: {key}')

# for key,value in sample_dict.items():
#     print(f'The dictionary key of "{key}" contains: {value}')

# Changing values
sample_dict["name"] = "Elliot"
# print(sample_dict)

# Deleting key-value pairs (entries)
del sample_dict["name"]
# print(sample_dict)

# 