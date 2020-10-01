import random

name = input("Enter your name : ")
print(f"Welcome {name} to play the guessing game!")
guess = False
num1 = random.randint(1,101)
counter = 0

while not guess:
    try:
        counter +=1
        num2 = int(input("Guess a number : "))
        if num1 == num2:
            print(f"The correct number is {num1}. You have guessed it right in {counter} attempts.")
            guess = True
        elif num1 < num2:
            print ("Your guess is too high")
        else:
            print ("Your guess is too low")
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")

   

