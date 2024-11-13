class Animal:
    def walk(self):
        return f'This animal is walking'
    
def send_help(name):
    return f'{name} needs urgent help.'

# Name confirmation
if __name__ == "__main__":
    animal = Animal()
    print(animal.walk())