cast = ['Harry', 'Ron', 'Hermoine', 'Severus']

for each_student in cast:
    if each_student == 'Severus':
        print(f'You are not welcome here, {each_student}')
    else:
        print(f'Welcome, {each_student}')

# Range Loops

for i in range(1,11):
    print(f'The number is: {i}')

# Getting min of

family = []
keep_asking = True

while keep_asking == True:
    member = input("What is yout nsmr. Press q to finish")
    