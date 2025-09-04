#Rock, Paper, Scissors Game
#Develop a simple Rock, Paper, Scissors game where the user plays against the computer. The game should declare a winner after each round.
import random
print("Welcome to Rock, Paper, Scissors Game!")
options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
rounds = int(input("Enter number of rounds you want to play: "))
for round in range(rounds):
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print("Invalid input, please try again.")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")
    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print("You win this round!")
        user_wins += 1
    else:
        print("Computer wins this round!")
        computer_wins += 1