# ASCII art for Rock, Paper, Scissors
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
# List of game options
game_opt = [rock, paper, scissors]

# Get user choice
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

# Display user choice or error if invalid
if 0 <= choice <= 3:
    print(game_opt[choice])
else:
    print("undefined")
  
# Random choice for computer
computer_choice = random.randint(0,2)

print("computer chose:")
print(game_opt[computer_choice])

# Determine winner
if  choice == computer_choice:
    print("Draw!")
elif  choice == 0 and computer_choice == 1:
    print("You Lose")
elif  choice == 0 and computer_choice == 2:
    print("You Win!")
elif  choice == 1 and computer_choice == 2:
    print("You Lose")
elif  choice == 1 and computer_choice == 0:
    print("You Win!")
elif  choice == 2 and computer_choice == 0:
    print("You Lose")
elif  choice == 2 and computer_choice == 1:
    print("You Win!")
else:
    print("Invalid input. Try again")

