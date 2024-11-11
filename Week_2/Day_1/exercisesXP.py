list_of_cats = []
oldest_cat = {
    'name': '',
    'age': 0
}

# Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

        list_of_cats.append({
            'name': cat_name,
            'age': cat_age
            })

cat1 = Cat("Megatron", 3)
cat2 = Cat("TIMOTHEEEEE", 420)
cat3 = Cat("Captain Sushi", 1)
cat4 = Cat("Serge", 5)

def find_oldest_cat():
    for cat in list_of_cats:
        if int(cat['age']) > oldest_cat['age']:
            oldest_cat['name'] = cat['name']
            oldest_cat['age'] = cat['age']

    return(f'The oldest cat is {oldest_cat['name']}, and is {oldest_cat['age']} years old.')

print(find_oldest_cat())