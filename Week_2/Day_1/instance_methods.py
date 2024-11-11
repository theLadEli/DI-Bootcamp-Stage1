class Dog:
    def __init__(self, dog_name):
        self.dog_name = dog_name
        print('A new dog has been initialised')
        print(f'His name is {dog_name}')

    def bark(self):
        print(f'{self.dog_name} has barked')

    def walk(self, distance):
        print(f'{self.dog_name} has walked {distance}km.')

    def rename(self, new_name):
        self.name = new_name
        print(f'{self.name} is now the dogs name.')
    
first_dog = Dog('Eli')

first_dog.bark()
first_dog.walk(10)

first_dog.rename('Spike')