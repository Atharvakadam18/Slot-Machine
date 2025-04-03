import random

r = random.randint(1, 50)
i = int(input("Guess a random number between 1 to 50: "))

while i != r:
    if(i == r):
        print("You have guessed the number !!!")
    elif(i > r):
        print("Your number is greater than random number")
    else:
        print("Your number is smaller than random number")
    i = int(input("Guess again: "))    

print("You have guessed the number !!!")