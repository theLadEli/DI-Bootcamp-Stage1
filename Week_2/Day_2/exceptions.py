try:
    my_num = input(int('Give me a number')) # If input a letter, it crashes code
except:
    raise TypeError('Please insert a valid number (0-9)')
    my_num = input(int('Give me a number'))