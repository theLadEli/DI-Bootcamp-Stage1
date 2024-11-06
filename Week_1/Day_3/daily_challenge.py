#challenge 1
words_by_user={}
word=input("Please enter a word ")
for index, letter in enumerate(word):
    if letter in words_by_user:
        words_by_user[letter].append(index)
    else:
        words_by_user[letter]=[index]
print(words_by_user)
#challenge2
grocery_dic={'water':'$5',
             'apples':'$20',
             'cucumbers':'$30',
             'chocolate':'$50'}
for key, value in grocery_dic.items():
    grocery_dic[key]=int(value.replace("$", ""))
print(grocery_dic)
affordable=[]
money_in_wallet=int(input("How much money do you have in your wallet?"))
for item, price in grocery_dic.items():
    if price <= money_in_wallet:
        affordable.append(item)
if not affordable:
        print("Nothing")
else:
        affordable.sort()
        print('Items that you can afford', affordable)