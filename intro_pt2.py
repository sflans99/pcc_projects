import random

# guest_list = ["Steven Gerrard", "Fernando Torres", "Virgil Van Dijk"]
# for name in guest_list:
#     print(f"Welcome {name} to the dinner party!")

# digits = []

# for value in range(1, 21):
#     print(value)

# 4-5 Million count

# milli = list(range(1, 1_000_000))
# print(sum(milli))

# 4-7 Threes
# multis = []
# for value in range(1, 11):
#     multis.append(value**3)
#     print(multis[-1])


# ---Loops Introduction---

# unconfirmed = ['a', 'b', 'c']
# confirmed = []

# while unconfirmed:
#     current_user = unconfirmed.pop()
#     print(current_user)

#     confirmed.append(current_user)

# ---Input Practice---

# name = input("Username:\n")
# message = input("Password:\n")

# print(f"Your username is:{name} \nYour password is:{message}")

# ---Multi-line Prompt---

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")


# ---Input Practice---
# height = input("How tall are you,in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nGrow you shrimp!")


# ---Multiples of Ten---
# user = int(input("Please guess a number:\n"))
# if user % 10 == 0:
#     print(f"{user} is a multiple of ten!")

# ---Loop Practice---
# prompt = "Enter a pizza topping:\n"
# prompt += "Type 'Quit' to end.\n"
# pizza = []
# while True:
#     toppings = input(prompt)
#     pizza.append(toppings)
#     print(pizza)
#     if toppings == "Quit":
#         break

# --- Filling Dict with Input---
# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("\nWhat is a mountain you want to climb?")

#     responses[name] = response

#     repeat = input("Let another person respond? Y/N")
#     if repeat == "N":
#         polling_active = False
    
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name.title()} wants to climb {response.title()}") 


# ---List and Input Practice---
# sandwich_list = ["Tuna", "Chicken Salad", "BLT", "Meatball"]
# finished_sandwiches = []
# while sandwich_list:
#     sip = sandwich_list.pop()
#     print(f"I just made {sip}")
#     finished_sandwiches.append(sip)

# for wich in finished_sandwiches:
#     print(f"{wich} was made.")


# ---Functions Practice---
# def greet_user(username):
#     """Displays a simple greeting."""
#     print(f"Hello {username.title()}!")

# greet_user('Sean')

# def daily_activity():
#     print("We are learning functions.")

# daily_activity()

# def favorite_book(book):
#     print(f"One of my favorite books is {book}")

# favorite_book('Aragon')


3 # ---Keyword Argument---
# def describe_pet(animal_type, animal_name):
#     print(f"I have a {animal_type}")
#     print(f"I have a {animal_type} named {animal_name}")

# describe_pet(animal_type="dog", animal_name="Jerry")

# ---Function Practice---
# 8-3 through 8-5
# def make_shirt(size="L", shirt_text="I love Python"):
#     print(f"You want to print a shirt, size {size} that says '{shirt_text}'")

# make_shirt()
# make_shirt(size='M')
# make_shirt(shirt_text='I really love Python', size='XL')


# def describe_city(city_name, country='United States of America'):
#     print(f"{city_name.title()} is in {country.title()}")

# describe_city(city_name='Dallas')
# describe_city(city_name='Florence', country='italy')
# describe_city('Houston')

# def get_formatted_name(first_name, last_name):
#     """Return a fully formatted name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('sonny', 'moore')
# print(musician)


# def city_country(city, country):
#     location = f"{city}, {country}".title()
#     return location

# print(city_country("St Louis", "USA"))
# print(city_country("Dallas", "USA"))

# def define_album(artist, album, songs=None):
#     full_album = {'Artist': artist, 'Album':album}
#     if songs != None:
#         full_album = {'Artist': artist, 'Album':album, 'Songs': songs}
    
#     return full_album

# create_album = define_album(['Skrillex', 'Diplo', 'Flux Pavillion'], 'Equinox', '10')
# print(create_album['Artist'][1])

# def show_messages(texts):
#     for text in texts:  
#         print(f"{text}")

# messages = ['Hello world!', 'What a time to be alive', 'Where the hell am I']
# show_messages(messages)

