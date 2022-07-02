# this program prompts the user for their name, then the name of their intended love and calculates the very scientific actual value of their compatibility.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

comp = (name1.replace(' ', "") + name2.replace(' ', "")).lower()

score1 = 0
score2 = 0

score1 += comp.count('t')
score1 += comp.count('r')
score1 += comp.count('u')
score1 += comp.count('e')
score2 += comp.count('l')
score2 += comp.count('o')
score2 += comp.count('v')
score2 += comp.count('e')

score = int(str(score1) + str(score2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
