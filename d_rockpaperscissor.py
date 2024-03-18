rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)______
           ________)
          _________)
         __________)
---._____________)
"""

scissor = """
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
"""

import random

game_images = [rock, paper, scissor]

user_choice = int(input('What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissor:'))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose:{computer_choice}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif computer_choice < user_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a Draw!")
