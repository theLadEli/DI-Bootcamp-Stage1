class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def display_info(self):
        super().display_info()
        print(f"School: {self.school}")

# Example objects
parent = Parent("John", 45)
child = Child("Alice", 12, "Greenwood High")

# Display information
parent.display_info()
child.display_info()