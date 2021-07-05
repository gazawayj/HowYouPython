from random import seed
from random import randint

print("What do I want to use Python for on this project?")
print("1. Create API/backend for the project.")
print("2. Attempt machine learning in order to do something pretty cool sounding.")
print("3. Choose one of the above randomly. That way I learn how to write random numbers in Python.")
print("4. Do options 3 and 2. In that order.")

#Random number generator seed creation and int grabbing
seed(894265426542)
randomSelection = randint(0,3)
print("You have randomly been selected option " + str(randomSelection))