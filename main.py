import time
import random
import scifi_DLC
import comedy_DLC 

#Functions
def death():
    print("Holy Crap! My Grandma is better at battling than ye!")
    time.sleep(2)
    print("GAME OVER")
    quit()

#Variables
hardcore = False

#This asks if the player wants to play hardcore mode
player_input = input("Do you want to play hardcore mode?  1 = yes/2 = no: ")
player_answered = False  # Initialize player_answered before the loop

while player_answered == False:
    try:
        player_input = int(player_input)  # Convert input to an integer
    except ValueError:
        print("Please enter a valid number (1 or 2).")
        player_input = input("Do you want to play hardcore mode?  1 = yes/2 = no: ")
        continue

    if player_input == 1:
        hardcore = True
        player_answered = True
    elif player_input == 2:
        hardcore = False
        player_answered = True
    else:
        print("Invalid choice. Please enter 1 or 2.")
        player_input = input("Do you want to play hardcore mode?  1 = yes/2 = no: ")


#This checks for dlc's and loads dlc's
player_input = input("type the name of the dlc if you don't have any type none.")
if player_input == "sci-fi":
    print("Loading DLC")
    time.sleep(1)
    scifi_DLC()
elif player_input == "comedy":
    print("Loading DLC")
    time.sleep(1)
    comedy_DLC()
else:
    # Intro
    time.sleep(1.5)
    print("Welcome to the arena")
    time.sleep(1)
    introAnswer = input("Now are ye goin to step into the arena an fight? 1 = yes  2 = no")
    if introAnswer == "1":
        time.sleep(0.5)
        print("Alright, yer not as wimpy as I thought. Now, step into the arena.")
    else:
        time.sleep(0.5)
        print("Ok, I ges yer runnin away like the coward ye are.")
        time.sleep(2)
        print("THE END")
        quit()
    time.sleep(2)
    print("Ok, welcome to the arena. To survive you must defeat many violent, merciless monsters.")
    time.sleep(1)
    # Battles Start
    # First Battle
    print("You see Grandpa Goblin. He is very short so you can just kick him like it's the opening of the Super Bowl")
    time.sleep(1)
    user_input = input("Type a number between 1 and 10.")
    random_int = random.randint(1, 10)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("O.K. But don't be too proud, my grandma fights better than ye an she's dead!")
    # Second Battle
    time.sleep(1)
    print("You see a zombie. Yup, just a zombie, so original.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 7.")
    random_int = random.randint(1, 7)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("Nice, but if ye keep braggin, I'm gonna pumbel you.")
    # Third Battle
    time.sleep(1)
    print("You see a possessed toilet, or what gen alphas call Skibidi Toilets.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 5.")
    random_int = random.randint(1, 5)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("A royal flush!")
    # Fourth Battle
    time.sleep(1)
    print("You see a knockoff Charizard named Fire Dragon.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 3.")
    random_int = random.randint(1, 3)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("I don't choose you, Fire Dragon!")
    # Fifth Battle
    time.sleep(1)
    print("FINAL BOSS!")
    time.sleep(1)
    print("You see a horrendous monster that is trying to eat the world, its name is...")
    time.sleep(0.75)
    print("HOMER SIMPSON!")
    time.sleep(1)
    user_input = input("Type a number between 1 and 2.")
    random_int = random.randint(1, 2)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("You have defeated the final boss!")
        time.sleep(0.75)
        print("You hear a loud DOH through the arena")
        time.sleep(3)
        print("YOU")
        time.sleep(0.75)
        print("HAVE")
        time.sleep(0.75)
        print("WON!")
        time.sleep(0.75)
    user_input = input("Wow! Good job, do you want to keep on fighting (hard mode)? 1 = Y 2 = n")
    # Hard Mode
    if user_input == "1":
        # First Hard Battle
        print("You see Grandpa Goblin. He is very short so you can just kick him like it's the opening of the Super Bowl")
        time.sleep(1)
        user_input = input("Type a number between 1 and 5.")
        random_int = random.randint(1, 5)
        if random_int == int(user_input):
            death()
        else:
            time.sleep(1)
            print("O.K. But don't be too proud, my grandma fights better than ye an she's dead!")
        # Second Hard Battle
        time.sleep(1)
        print("You see a zombie. Yup, just a zombie, so original.")
        time.sleep(1)
        user_input = input("Type a number between 1 and 4.")
        random_int = random.randint(1, 4)
        if random_int == int(user_input):
            death()
        else:
            time.sleep(1)
            print("Nice, but if ye keep braggin, I'm gonna pummel you.")
        # Third Hard Battle
        time.sleep(1)
        print("You see a possessed toilet, or what gen alphas call Skibidi Toilets.")
        time.sleep(1)
        user_input = input("Type a number between 1 and 3.")
        random_int = random.randint(1, 3)
        if random_int == int(user_input):
            death()
        else:
            time.sleep(1)
            print("A royal flush!")
        # Fourth Hard Battle
        time.sleep(1)
        print("You see a knockoff Charizard named Fire Dragon.")
        time.sleep(1)
        user_input = input("Type a number between 1 and 2.")
        random_int = random.randint(1, 2)
        if random_int == int(user_input):
            death()
        else:
            time.sleep(1)
            print("I don't choose you, Fire Dragon!")
        # Fifth Hard Battle
        time.sleep(1)
        print("FINAL BOSS!")
        time.sleep(1)
        print("You see a horrendous monster that is trying to eat the world, its name is...")
        time.sleep(0.75)
        print("HOMER SIMPSON!")
        time.sleep(1)
        user_input = input("Type a number between 1 and 5.")
        random_int = random.randint(1, 5)
        if random_int == int(user_input):
            time.sleep(1)
            print("You have defeated the final boss!")
            time.sleep(0.75)
            print("You hear a loud DOH through the arena")
            time.sleep(3)
            print("YOU")
            time.sleep(0.75)
            print("HAVE")
            time.sleep(0.75)
            print("WON!")
            time.sleep(0.75)
            quit()
        else:
            death()
    else:
        quit()