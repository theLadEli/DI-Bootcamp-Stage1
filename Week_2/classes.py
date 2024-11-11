# Classes need to be started with a capital letter
# Dont attribute certain parameters dont need to put the brackets if no classes

class Dogs():
    def __init__(self, name, height):
        self.name = name
        self.height = height
        print(f'{name} is {height}cm')
        

def add_dog():
    Dogs("Ness",22)

add_dog()