import random

# Exercise 1
my_fav_numbers = {18,27,36,45,34}

my_fav_numbers.add(1)
my_fav_numbers.add(420)

print(my_fav_numbers)

friend_fav_numbers = {68,2,990,23}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

# Exercise 2
# No

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.pop(basket.index("Banana"))
basket.pop(basket.index("Blueberries"))
basket.append("Kiwi")
basket.insert(0, "Apples")
num_apples = 0

for fruit in basket:
    if fruit == "Apples":
        num_apples = num_apples+1

print(num_apples)
print(basket)

basket.clear()
print(basket)

# Exercise 4
your_floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
my_floats = []


while len(my_floats) < 10:
    ran_float = random.random()*10
    my_floats.append(round(ran_float,2))

print(my_floats)

# Exercise 5
for i in range(1,21):
    print(i)

for i in range(1,21):
    if (i % 2 == 0):
        print(i)

# Exercise 6
my_name = "Eli"
same_name = False

while same_name == False:
    your_name = input("What is your name?")
    if (your_name == my_name):
        same_name = True

# Exercise 7
fav_fruits = input("What is your favourite fruits? Separate multiple using space key.")

fav_fruits = fav_fruits.split()

extra_fruit = input("Input any fruit")
same_fruit = False

for fruit in fav_fruits:
    if (extra_fruit == fruit):
        same_fruit = True
    else:
        same_fruit = False


if (same_fruit == True):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8
ask_toppings = True
pizza_toppings = []
pizza_price = 10

while ask_toppings == True:
    new_topping = input("Input your favourite pizza toppings")

    if (new_topping == 'quit'):
        ask_toppings = False
    else:
        pizza_toppings.append(new_topping)

print(pizza_toppings)
num_toppings = pizza_toppings.count()
pizza_price = pizza_price + (num_toppings*2.5)
print(f'Your pizza costs ${pizza_price}')