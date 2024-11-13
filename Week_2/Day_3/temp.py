import faker
users = []
fake = Faker()

def users_added():
    user = {
        'name': fake.name(), 
        'address': fake.address(),
        'language_code': fake.language_code()  
    }
    
    users.append(user)

users_added()   
users_added()
users_added()

for er in users:
    print(er)