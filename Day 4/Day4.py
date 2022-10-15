import random

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


print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

player_choice = int(input())

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Invalid number, you lose!")

computer_choice = random.randint(0, 2)

print("Computer chose " + str(computer_choice))

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)


if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw")
