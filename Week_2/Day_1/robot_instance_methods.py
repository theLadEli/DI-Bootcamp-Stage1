class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        print('Robot initialised')
    
    def introduce_self(self):
        print(f'My name is {self.name}, I am a {self.color} robot that weighs {self.weight}kg.')

class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned
    
    def sit_down(self):
        if self.isSitting:
            print("I am already sitting.")
        else:
            print("I have sat down.")
            self.isSitting = True

    def stand_up(self):
        if not self.isSitting:
            print("I am already standing.")
        else:
            self.isSitting = False
            print("I have stood up")

r1 = Robot("Tom", "red", 48)
r1.introduce_self()

p1 = Person("Eli", "Can't sit still", False, r1)
print(p1.isSitting)
p1.sit_down()
print(p1.isSitting)
p1.sit_down()
p1.stand_up()