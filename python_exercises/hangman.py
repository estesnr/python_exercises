# UNFINISHED

import random
word_list = ['greatsword', 'magician', 'blanket']
chosen_word = random.choice(word_list)
print('Welcome to Hangman!')
print(f'chosen word is {chosen_word}')
word_length = len(chosen_word)
display = []
for blank in range(0, word_length):
    display += "_"
    
print(f"{' '.join(display)}")  

lives = 6

guess = input('Guess a letter: ').lower()


end_of_game = False 
   
while end_of_game == False:
    guess = input('Guess a letter: ').lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess: 
            display[position] = letter
            print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game == True
            print('You Win')
            print(f"{' '.join(display)}")

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game == True
        print('You Lose')
