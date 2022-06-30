#Data Types

print('Welcome to the Tip Calculator')

bill = input('What was the total bill?')

perc = input('How much tip do you want to leave?')

peeps = input('How many people are splitting the bill?')

each_pay = ((int(bill) * (int(perc)/100)) + int(bill)) / int(peeps)

final_bill = '{:.2f}'.format(each_pay)

print(f"Each person should pay ${final_bill}")
