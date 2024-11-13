from modules import send_help, Animal
import random
import pygame

class Cat(Animal):
    pass

my_cat = Cat()
print(my_cat.walk())

print(send_help('Eli'))
print(random.randint(1,10))

