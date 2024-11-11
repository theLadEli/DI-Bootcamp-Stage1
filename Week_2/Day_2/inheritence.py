## Multi Level Inheritance

# class Grandpa:
#     def speak(self):
#         print("Grandpa is speaking.")
    
#     def sleep(self):
#         print("Grandpa is sleeping.")

# class Parent(Grandpa):
#     def speak(self):
#         print("Parent is speaking.")

# class Child(Parent):
#     pass

# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj2.speak()    # This will print the Parents `speak` as that is the closest relation to the child
# obj2.sleep()

## Multiple Inheritance

class Parent1:
    def speak(self):
        print("Parent is speaking.")
    
    def eat(self):
        print("Parent1 is eating cake.")

class Parent2:
    def speak(self):
        print("Parent2 is speaking.")

class Child(Parent2, Parent1):   # The order here will define which inheritance takes priority
    pass


obj2 = Child()
obj2.speak()    # This will print from 'Parent2' as it is the first inheritance specified in 'Child'
obj2.eat()  # This will print from 'Parent1' as it is the only inheritance with 'eat()'