# Defining a function
def say_hello():
    print('Hello Python')

# Calling the function
say_hello()

# Defining a function with arguments
def greet(greeting):
    print(f'{greeting} Python')

greet('Shalom')

# Defining a function with multiple arguments
def greet_language(name, language):
    if language == 'PT':
        print(f'Ola, {name}')
    elif language == 'HE':
        print(f'Shalom, {name}')
    elif language == 'EN':
        print(f'Hello, {name}')

greet_language('Eli', 'HE')

# Setting a default value
def greet_language(name, language = 'PT'):
    if language == 'PT':
        print(f'Ola, {name}')
    elif language == 'HE':
        print(f'Shalom, {name}')
    elif language == 'EN':
        print(f'Hello, {name}')

greet_language('Eli')

# Using Global Variables in Functions
global_var = 100

def calculation(a,b):
    global global_var
    addition = a+b
    substraction = a-b
    global_var += addition
    print(f'Addition = {addition}\nSubtraction = {substraction}')
    print(f'Global Variable + Addition = {global_var}')

calculation(5,7)

