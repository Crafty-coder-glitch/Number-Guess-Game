import random

num = random.randint(0,100)
guess = None
while guess!= num:
    guess = input("your guess:")
    guess = int(guess)
if guess == num:
    print("You Win!")
# this program shall work in a loop until the number guessed is equal to the input of the user