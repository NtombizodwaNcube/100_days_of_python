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

user_choice = input("Enter a choice (rock, paper, scissors): ")
possible_outcomes = ["rock", "paper", "scissors"]
auto_choice =random.choice(possible_outcomes)
print(f"\nYou chose {user_choice}, computer chose {auto_choice}.\n")

if user_choice == auto_choice:
  print(f"Both players chose{user_choice} It's a tie")
elif user_choice == "rock":
  if auto_choice == "scissors":
    print("Rock smashes scissors. You lose.")
  else:
    print("Paper covers rock you. You lose")

elif user_choice == "paper":
  if auto_choice == "rock":
    print("Paper covers rock. You win")
  else:
    print("Scissors cuts paper. You lose")
elif user_choice == "scissors":
  if auto_choice == "paper":
    print("Scissors cuts paper. You win")
  else:
    print("Rock smashes scissors. You lose")
  
  