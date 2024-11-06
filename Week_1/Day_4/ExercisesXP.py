import random

# Exercise 1
def display_message():
    print('I am learning Python in Developers Institute.')

display_message()

# Exercise 2
def favourite_book(title):
    print(f'One of my favourite books is {title}.')

favourite_book(1984)

# Exercise 3
def describe_city(city,country = "Britain"):
                                # Default is britain as we colonised most :D
    print(f'{city} is in {country}.')

describe_city("Tel Aviv")

# Exercise 4
# I added an if/else statement to tell the user how many digits away their guess was.

def random_num(number):
    correct_random_num = random.randint(0,99)

    if number == correct_random_num:
        print(f'Our number was {correct_random_num}, you chose {number}.\nYou input the exact correct value! 🎉')
    else:
        num_difference = 0

        if correct_random_num > number:
            num_difference = correct_random_num - number
        elif number > correct_random_num:
            num_difference = number - correct_random_num

        print(f'Our number was {correct_random_num}, you chose {number}.\n🛑 You input the wrong value and were {num_difference} away.')

random_num(int(input("Input a random number between 1-100")))

# Exercise 5
def make_shirt(size = "l", message = "I love Python"):
    print(f'The size of the shirt is {size} and the text is {message}.')

make_shirt("m")
make_shirt("xxs", '"\'This is nice\' - Borat"')

my_size = "xxs"
shirt_slogan = "Great Success!"
make_shirt(my_size,shirt_slogan)

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for i in magician_names:
        print(i)

show_magicians()

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = str(f'The great {magician_names[i]}')
    print(magician_names)

make_great()
show_magicians()

# Exercise 7
def get_random_temp(season):
    season = season.lower()

    if season == 'winter':
        return(round(random.uniform(-11,10),2))
    if season == 'spring':
        return(round(random.uniform(5,15),2))
    if season == 'summer':
        return(round(random.uniform(20,36),2))
    if season == 'autumn':
        return(round(random.uniform(5,15),2))

def main():
    user_season = input("What season do you want temperatures on?")
    celcius = get_random_temp(user_season)

    if celcius < 0:
        print('It\'s bloody freezing outside!')
    elif celcius >= 0 and celcius < 16:
        print('Almost like a heatwave in Britain!')
    elif celcius >= 16 and celcius < 23:
        print('Britain knows nothing like this...')
    elif celcius >= 23 and celcius < 33:
        print('This is what I came to Israel for!')
    elif celcius >= 33 and celcius < 40:
        print('Maybe global warming is a thing...')

    print(f'The temprature now is {celcius} degrees Celcius.')

main()

# Exercise 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

answ_correct = []
answ_incorrect = []

def questionnaire():
    for i in data:
        user_answer = input(i["question"]).lower()
        if user_answer == i["answer"].lower():
            answ_correct.append(i)
        else:
            answ_incorrect.append(i)
    
    print(f'Game Over!\n✅ Total Correct: {len(answ_correct)}\n❌ Total Incorrect: {len(answ_incorrect)}')
    check_score()

def check_score():
    if len(answ_incorrect) > 3:
        print('You got more then three incorrect, try again.')
        questionnaire()

questionnaire()