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

#Battles Start
print("You see Grandpa Goblin. He is very short so you can just kick him like its the opening of the Super Bowl")
input("Type a number between 1 and 20.")
random_int = random.randint(1,20)
if random_int == input:
    death()
else:
    time.sleep(1)
    print("O.K. But dont be to proud, my grandma fights better then ye an she's dead!")