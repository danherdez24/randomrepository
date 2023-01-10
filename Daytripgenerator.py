
import random


Destinations = ["California", "Texas", "Alaska", "Nevada"]

Restaurants = ["In N Out", "Buccees", "Ginger", "Hell's Kitchen"]

Transportation = ["Airplane", "Car", "Cruise", "Bus"]

Entertainment = ["Hiking", "Spa Day", "Gun Range", "Gambling"]

def vacation_selections():
    destination = random.choice(Destinations)

    restaurant = random.choice(Restaurants)

    transport = random.choice(Transportation)

    entertain = random.choice(Entertainment)

    return[destination, restaurant, transport, entertain]


def vacation_selected():
    confirm_bool = True
    while confirm_bool:
        vacation = vacation_selections()
        user_input = input(f"We have selected {vacation[0]} {vacation[1]} {vacation[2]} {vacation[3]} Do you accept (y/n)?" )
        if user_input == "n":

            return vacation_selected()
        else:
            confirm_bool = False

            print(user_input)
    print(f"Congratulations! You're going on {vacation[0]} {vacation[1]} {vacation[2]} {vacation[3]} ")
vacation_selected()