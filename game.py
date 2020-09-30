"""A number-guessing game."""

# Put your code here 
from random import randint

name = input('Greetings, what is your name? : ')
print(f'Hi, {name}')

target_number = randint(1,100)
guess = int(input(f'{name}, please choose a number between 1 and 100. : '))
counter = 0


while not guess == target_number:
    counter += 1
    if guess < target_number:
        guess = int(input('We\'re sorry, your guess is too low. Please try again. : '))
    elif guess > target_number:
        guess = int(input('We\'re sorry, your guess is too high. Please try again. : '))


print(f'Congratulations {name}, {guess} is indeed the target.')
print(f'You completed the game in {counter + 1} tries.') 