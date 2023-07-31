import random

def get_choices():    
    player_choice = input("Enter a choice: rock, paper, scissors: ")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    print(computer_choice)
    choices = {"player": player_choice, "computer":     
    computer_choice}
    return choices

def check_win(player, computer):
  print(f"You chose {player} and the computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return "Rock beats scissors. Player wins"
    else: 
      return "Paper beats Rock. Computer wins"
  elif player == "paper":
    if computer == "rock":
      return "Paper beats Rock. Player wins"
    else: 
      return "Scissors beats Paper. Computer wins"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors beats Paper. Player wins"
    else: 
      return "Rock beats Scissors. Computer wins"  

choices = get_choices()
results = check_win(choices["player"], choices["computer"])
print(results)
