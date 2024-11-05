import random

# # Exercise 1
# my_fav_numbers = {18,27,36,45,34}

# my_fav_numbers.add(1)
# my_fav_numbers.add(420)

# print(my_fav_numbers)

# friend_fav_numbers = {68,2,990,23}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# print(our_fav_numbers)

# # Exercise 2
# # No

# # Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.pop(basket.index("Banana"))
# basket.pop(basket.index("Blueberries"))
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# num_apples = 0

# for fruit in basket:
#     if fruit == "Apples":
#         num_apples = num_apples+1

# print(num_apples)
# print(basket)

# basket.clear()
# print(basket)

# # Exercise 4
# your_floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# my_floats = []


# while len(my_floats) < 10:
#     ran_float = random.random()*10
#     my_floats.append(round(ran_float,2))

# print(my_floats)

# # Exercise 5
# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if (i % 2 == 0):
#         print(i)

# # Exercise 6
# my_name = "Eli"
# same_name = False

# while same_name == False:
#     your_name = input("What is your name?")
#     if (your_name == my_name):
#         same_name = True

# # Exercise 7
# fav_fruits = input("What is your favourite fruits? Separate multiple using space key.")

# fav_fruits = fav_fruits.split()

# extra_fruit = input("Input any fruit")
# same_fruit = False

# for fruit in fav_fruits:
#     if (extra_fruit == fruit):
#         same_fruit = True
#     else:
#         same_fruit = False


# if (same_fruit == True):
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# # Exercise 8
# ask_toppings = True
# pizza_toppings = []
# pizza_price = 10

# while ask_toppings == True:
#     new_topping = input("Input your favourite pizza toppings, input 'quit' to exit")

#     if (new_topping == 'quit'):
#         ask_toppings = False
#     else:
#         pizza_toppings.append(new_topping)

# print(pizza_toppings)
# num_toppings = len(pizza_toppings)
# pizza_price = pizza_price + (num_toppings*2.5)
# print(f'Your pizza costs ${pizza_price}')

# Exercise 9
# total_cost = 0
# family_members_loop = 0
# family_members = 0

# family_members = int(input("How many members are in your family?"))

# while family_members_loop != family_members:
#     age = int(input("Input the age of the family member."))

#     if (age < 3):
#         total_cost = total_cost + 0
#     elif (age < 12):
#         total_cost = total_cost + 10
#     elif (age >= 12):
#         total_cost = total_cost + 15

#     family_members_loop = family_members_loop+1

# print(f"The total ticket costs is ${total_cost}")

# # Exercise 9.4
# teenager_names = []
# loop_name_input = True

# while loop_name_input == True:
#     teen_name = input("Hello, what is your name? To exit the loop, enter 'quit'")

#     if teen_name == "quit":
#         loop_name_input = False
#     else:
#         teen_age = int(input(f'Hello {teen_name}, how old are you?'))
#         if teen_age > 16:
#             teenager_names.append(teen_name)

# print(teenager_names)

# Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]