

#Project: A Number Guess Game
# This program only breaks when you either enter the correct number or reach the maximum attempts. 

from random import randint

username=input("What is your name: ")

#"{username[0].upper() + username[1:].lower()}": Ensuring the user's input returns the initial as a capital letter.
print(f"Welcome {username[0].upper() + username[1:].lower()}😊! Take a number guess between 1 and 100")

secretNumber=randint(1, 100)

attempts=0

while True: 
    try: 
        guess = int(input('Take a number guess: '))
        attempts += 1
        if guess < secretNumber:
            print("Number too low")
        elif guess > secretNumber:
            print("Number too high")
        else: 
            print(f"Correct! Congratulation {username[0].upper() + username[1:].lower()}, You guessed the number in {attempts} attempts.")
            break
        if attempts >= 10: 
            print(f"{attempts} Maximum attempts reached! Try more, {username[0].upper() + username[1:].lower()}. Enjoyyyy")
            break
    except (ValueError, KeyboardInterrupt): 
        print("No letter! No keyboard C' key")
        continue

    
    









