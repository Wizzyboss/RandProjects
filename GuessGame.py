
# Using for loop to play a computer guess game. 

import random

print('Enter your name: ')
name = input(str())
print('Hello, ' + name + '. I\'m thinking of a number between 1 and 20' )

secretNumber = random.randint(1, 20)

for guessTaken in range(1, 8):
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('Number too high')

    elif guess < secretNumber:
        print('Number too low')

    else:
        break


if guess == secretNumber:
    print('Congrats, ' + name +'!' + ' You guessed my number in ' + str(guessTaken) + ' times.')


else:
    print(f'Nope, maximum attempts reached in {guessTaken} times! I was thinking of the number ' + str(secretNumber ))










