import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print("Let's play Rock, Paper, Scissors!")
player_choice = input("Choose one: rock, paper, or scissors? ").lower()

print(f"You chose {player_choice}, and the computer chose {computer_choice}.")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")