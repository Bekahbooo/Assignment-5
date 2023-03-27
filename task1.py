# Rebekah Gardner-Assignment 5-Task 1-Period 3

#Imports the random library
import random

#Selects a random number
num = random.randint(1,10)

#Tells user instructions and starts the game
print("Welcome to the Guessing Game")
print("The Computer has picked a number from 1 - 10. Try to match it.")
guess = int(input("What number do you choose (1-10): "))

#decides how close the user was
if guess == num:
    msg = "Honored to play with you, Master."
elif abs(guess - num) == 1:
    msg = "You are a worthy opponent, Knight."
elif abs(guess - num) == 2:
    msg = "You have much to learn, Padawan."
elif abs(guess - num) == 3:
    msg = "Youngling, your time will come."
else:
    msg = "Keep working hard in the Service Corps."

#tells user how close they were
print("You picked " + str(guess) + ", and the actual number was " + str(num) + ".")
print(msg)












