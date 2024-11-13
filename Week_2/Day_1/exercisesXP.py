# # Exercise 1
# list_of_cats = []
# oldest_cat = {
#     'name': '',
#     'age': 0
# }

# # Exercise 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

#         list_of_cats.append({
#             'name': cat_name,
#             'age': cat_age
#             })

# cat1 = Cat("Megatron", 3)
# cat2 = Cat("TIMOTHEEEEE", 420)
# cat3 = Cat("Captain Sushi", 1)
# cat4 = Cat("Serge", 5)

# def find_oldest_cat():
#     for cat in list_of_cats:
#         if int(cat['age']) > oldest_cat['age']:
#             oldest_cat['name'] = cat['name']
#             oldest_cat['age'] = cat['age']

#     return(f'The oldest cat is {oldest_cat['name']}, and is {oldest_cat['age']} years old.')

# print(find_oldest_cat())

# # Exercise 2
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f'{self.name} goes woof!')
    
#     def jump(self):
#         print(f'{self.name} jumps {self.height*2}cm high!')

# davids_dog = Dog('Rex',10)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup',20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     print(f'{sarahs_dog.name} is taller!')
# elif davids_dog.height > sarahs_dog.height:
#     print(f'{davids_dog.name} is taller!')
# else:
#     print(f'{sarahs_dog.name} and {davids_dog.name} are the same height!')

# # Exercise 3
# class Song:
#     def __init__(self, lyrics = []):
#         self.lyrics = lyrics
    
#     def sing_me_a_song(self):
#         for i in self.lyrics:
#             print(i)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# # Exercise 4
class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if self.animals(animal_sold) == True:
            self.animals.remove(animal_sold)
            print(f'{animal_sold} has been sold.')
        else:
            print(f'You do not have a {animal_sold}\'s to sell.')


ramat_gan_zoo = Zoo("Ramat Gan Zoo")
ramat_gan_zoo.add_animal("Lion")
ramat_gan_zoo.add_animal("Bearded Dragon")
ramat_gan_zoo.get_animals()

ramat_gan_zoo.sell_animal("Lion")
# ramat_gan_zoo.sell_animal("Tiger")