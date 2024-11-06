# Changing all the values of dictionary with dict comprehension
family_age = {'Eli': 17, 'Rafi': 22, 'Tami': 23, 'Zevi': 24}
new_ages = {name:age + 1 for (name,age) in family_age.items()}

print(new_ages)