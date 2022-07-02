# little choose your own adventure game to practice conditionals.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_move = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'.").lower()

if first_move == "left":
  second_move = input('You have come to a lake. There is an island in the middle of the lake. Do you want to "wait" for a boat, or "swim" across the lake yourself?').lower()
  if second_move == 'wait': 
    third_move = input('You arrive at the island unharmed. There is a house with 3 doors. You can go through the "red" one, the "blue" one, or the "yellow" one. Which do you choose?').lower()
    if third_move == 'red':
      print('You are engulfed by flames. Game Over.')
    elif third_move == 'blue':
      print('You are devoured by an enormous Beast. Game Over.')
    elif third_move == 'yellow':
      print('You have claimed the treasure! You win!')
    else: 
      print('You have broken the rules of Treasure Island. You are torn apart by Mustakrakish, the Lake Troll.')
  else:
    print('Attacked by a trout. Game Over.')
else:
  print('Fall into a hole. Game Over.')
