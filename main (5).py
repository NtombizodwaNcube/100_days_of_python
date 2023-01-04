rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_outcomes = ["rock", "paper", "scissors"]
auto_player =random.choice(possible_outcomes)
print(f"\nYou chose {user_action}, computer chose {auto_player}.\n")

if user_action == auto_player:
  print(f"Both players chose{user_action} It's a tie")
elif user_action == "rock":
  if auto_player == "scissors":
    print("Rock smashes scissors. You lose.")
  else:
    print("Paper covers rock you. You lose")

elif user_action == "paper":
  if auto_player == "rock":
    print("Paper covers rock. You win")
  else:
    print("Scissors cuts paper. You lose")
elif user_action == "scissors":
  if auto_player == "paper":
    print("Scissors cuts paper. You win")
  else:
    print("Rock smashes scissors. You lose")
  
  