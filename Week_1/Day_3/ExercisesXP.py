# # Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# print(dict(zip(keys, values)))

# # Exercise 2
# cost = 0
# family = {}
# loop_fam = True

# while loop_fam == True:
#     new_fam_name = input("What is the name of the family member? Input 'quit' to finish.")

#     if new_fam_name == 'quit':
#         loop_fam = False
#     else:
#         new_fam_age = int(input(f"How is old {new_fam_name}?"))
#         family[new_fam_name] = new_fam_age
# print(family)

# for i in family:
#     i_age = family[i]

#     if i_age < 3:
#         print(f'{i} has to pay $0.')
#     elif i_age < 12:
#         print(f'{i} has to pay $10.')
#         cost += 10
#     elif i_age >= 12:
#         print(f'{i} has to pay $15.')
#         cost += 15

# print(f'The total family cost is ${cost}')

# # Exercise 3
# zara = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'],
#     'number_stores': 7000,
#     'major_color': {
#         'France': 'blue',
#         'Spain': 'red',
#         'US': ['pink', 'green']
#     }
# }

# zara['number_stores'] = 2

# zara['country_creation'] = 'spain'

# if 'international_competitors' in zara:
#     zara['international_competitors'].append('Desigual')

# zara.pop('creation_date')

# print(zara['international_competitors'][-1])
# print(zara['major_color']['US'])
# print(len(zara))
# print(zara.keys())

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }

# zara = {**zara,**more_on_zara}

# print(zara['number_stores'])

# # Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
disney_users_D = {}
disney_users_E = {}
counter_A = 0
counter_B = 0
counter_C = 0
counter_D = 0
counter_E = 0

for i in users:
    disney_users_A[i] = counter_A
    counter_A += 1

for i in users:
    disney_users_B[counter_B] = i
    counter_B += 1

users_sorted = sorted(users)

for i in users_sorted:
    disney_users_C[i] = counter_C
    counter_C += 1

for i in users:
    if (i.find('i') == True):
        disney_users_D[i] = counter_D
        counter_D += 1

for i in users:
     if i[0] == 'M' or i[0] == 'P':
        disney_users_E[i] = counter_E
        counter_E += 1
         

print(disney_users_E)