#libraries
import time

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
