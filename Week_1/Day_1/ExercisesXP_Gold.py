# Exercise 1
print(f"{'Hello world \n'*4}{'I love python \n'*4}")

# Exercise 2
user_month = int(input("Input a month (1-12)"))

if user_month >= 3 and user_month <= 5:
    print("Spring")
elif user_month >= 6 and user_month <= 8:
    print("Summer")
elif user_month >= 9 and user_month <= 11:
    print("Autumn")
elif user_month >= 12 and user_month <= 2:
    print("Winter")