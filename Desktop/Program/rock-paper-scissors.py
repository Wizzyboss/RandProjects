

import random

print("Welcome to Rock, Paper, Scissors!")

def play_game():
    choices = ["rock", "paper", "scissors"]

    player = 0
    computer = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose {player_choice}. The computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            player += 1
        else:
            print("Computer wins!")
            computer += 1
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"You won {player} times")
    print(f"Computer won {computer} times")



play_game()

