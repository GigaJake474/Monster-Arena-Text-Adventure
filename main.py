#libraries
import time
import random

#Functions
def death():
    print("Holy Crap! My Grandma is better at battling then ye!")
    time.sleep(2)
    print("GAME OVER")

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
    exit(1)

time.sleep(2)
print("Ok, welcome to the arena. To survive you must defeat many violent, merciless monsters.")
time.sleep(1)

#Battles Start

#First Battle
print("You see Grandpa Goblin. He is very short so you can just kick him like its the opening of the Super Bowl")
time.sleep(1)
input("Type a number between 1 and 10.")
random_int = random.randint(1,10)
if random_int == input:
    death()
else:
    time.sleep(1)
    print("O.K. But dont be to proud, my grandma fights better then ye an she's dead!")

#Second Battle
time.sleep(1)
print("You see zombie. Yup just a zombie, so original.")
time.sleep(1)
input("Type a number between 1 and 7.")
random_int = random.randint(1,7)
if random_int == input:
    death()
else:
    time.sleep(1)
    print("Nice, but if ye keep braggin, im gonna pumble you.")

#Third Battle
time.sleep(1)
print("You see a posessed toilet, or what gen alphas call Skibidi Toilets.")
time.sleep(1)
input("Type a number between 1 and 5.")
random_int = random.randint(1,5)
if random_int == input:
    death()
else:
    time.sleep(1)
    print("A royal flush!")

#Fourth Battle
time.sleep(1)
print("You see a knockoff Charzard named Fire Dragon.")
time.sleep(1)
input("Type a number between 1 and 3.")
random_int = random.randint(1,3)
if random_int == input:
    death()
else:
    time.sleep(1)
    print("I don't choose you Fire Dragon!")

#Fith Battle
time.sleep(1)
print("FINAL BOSS!")
time.sleep(1)
print("You see a horendous monster that is trying to eat the world, its name is...")
time.sleep(0.75)
print("HOMER SIMPSON!")
time.sleep(1)
input("Type a number between 1 and 2.")
random_int = random.randint(1,2)
if random_int == input:
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