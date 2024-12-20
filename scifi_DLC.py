#libraries
import time
import random

# Functions
def death():
    print("Dank Farrik! I can't belive I bet 100 Space-Bucks on you!")
    time.sleep(2)
    print("GAME OVER")
    quit()

#The DLC
def scifi_DLC():
    # Intro
    time.sleep(1.5)
    print("Welcome to alien arena.")
    time.sleep(1)
    introAnswer = input("Now are ye goin to step into the arena an fight? 1 = yes  2 = no")

    if introAnswer == "1":
        time.sleep(0.5)
        print("Ok, now get in the arena cause I can put you in warm or I can put you in cold..")
    else:
        time.sleep(0.5)
        print("Ok, I guess your going in cold.")
        time.sleep(2)
        print("THE END")
        quit()

    time.sleep(2)
    print("Ok, welcome to the arena. To survive you must defeat many viscious aliens and otherworldly monsters.")
    time.sleep(1)

    # Battles Start

    # First Battle
    print("You see Kang and Kodos and they look very hangry.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 10.")
    random_int = random.randint(1, 10)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("O.K. well they got outsmarted by Homer Simpson, so don't be to proud.")

    # Second Battle
    time.sleep(1)
    print("You see Wall-E, yup that really stupid robot.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 7.")
    random_int = random.randint(1, 7)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("I'm gonna pumbel you.")

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
    print("You see Pizza The Hut. You also become very hungry.")
    time.sleep(1)
    user_input = input("Type a number between 1 and 3.")
    random_int = random.randint(1, 3)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("Pizza Party")

    # Fifth Battle
    time.sleep(1)
    print("FINAL BOSS!")
    time.sleep(1)
    print("You see a dark figure aproach you.")
    time.sleep(0.75)
    print("It's Dark Helmet!")
    time.sleep(1)
    user_input = input("Type a number between 1 and 2.")
    random_int = random.randint(1, 2)
    if random_int == int(user_input):
        death()
    else:
        time.sleep(1)
        print("You used the schwartz and defeated Dark Helmet!")
        time.sleep(0.75)
        print("Use The Schwartz!")
        time.sleep(3)
        print("YOU")
        time.sleep(0.75)
        print("HAVE")
        time.sleep(0.75)
        print("WON!")
        time.sleep(0.75)
