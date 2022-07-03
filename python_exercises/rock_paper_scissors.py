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
import math
user_input = int(input('Which do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n'))
if user_input == 0:
  user = rock
elif user_input == 1:
  user = paper
elif user_input == 2:
  user = scissors

comp_input = math.floor(random.randint(0, 2))
if comp_input == 0:
  comp = rock
elif comp_input == 1:
  comp = paper
elif comp_input == 2:
  comp = scissors


if comp_input == user_input:
  print(f"You chose {user}, opponent chose {comp}. Draw!")
elif (comp_input == 0 and user_input == 1) or (comp_input == 1 and user_input == 2) or (comp_input == 2 and user_input == 0):
  print(f"You chose {user}, opponent chose {comp}. You win!")
else:
  print(f"You chose {user}, opponent chose {comp}. You lose!")
