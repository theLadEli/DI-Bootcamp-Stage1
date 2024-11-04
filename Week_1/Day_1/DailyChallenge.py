user_string = input("Input a 10 character string")

if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
elif len(user_string) == 10:
    print("Perfect string.")

print(user_string[0])
print(user_string[len(user_string)-1])

user_string_as_list = list(user_string)
for i in user_string_as_list:
    print(i)