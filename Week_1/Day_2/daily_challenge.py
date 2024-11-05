#challenge 1 
number=int(input("Enter a number"))
number_length=int(input("Enter the length ex; how many numbers you want"))

empty=[]
num=0
while len(empty)<number_length:
    num+=number
    empty.append(num)

print(empty)

#challenge 2
text=input("Please enter a string")
text_list = list(text)
final_list = []
seen=set()

for i in text_list:
    if i not in seen:
        seen.add(i)
        final_list.append(i)

        
final = ''.join(final_list)
print(final)