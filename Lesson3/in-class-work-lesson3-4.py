# 19. Question: Guess the Number Game
# The computer generates a random number using the following code:
# import random
# secret_number = random.randint(1, 100)
# Write a Python program that asks the user to guess the number.
# Rules:
# The user enters a number.
# If the guess is smaller than the secret number, print "Too small".
# If the guess is greater than the secret number, print "Too big".
# If the guess is correct, print "Correct! You found the number" and stop the program.
# Use a while loop so the game continues until the correct number is guessed.
# In short: the computer chooses a random number between 1 and 10, and the user keeps guessing until they find it.




import random

secret = random.randint(1,100)

entered_value = int(input("Enter a number: "))

while entered_value != secret:
    if entered_value > secret:
        print("Too big!")
    else:
        print("Too small!")
    entered_value = int(input("Enter a number: "))
else:
    print("Congrats!")