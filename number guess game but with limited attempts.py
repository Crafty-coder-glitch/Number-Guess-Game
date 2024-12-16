import random
num = random.randint(0,100)
print("try guessing the number between 0 to 100 in 15 attempts")
for _ in range(15):
    guess=int(input("enter value:"))
    guess=int(guess)
if guess==num:
    print("you win")
else:
    print("you lose")
 
