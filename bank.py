#Weekly task 02
#The program prompts the user and read in two money amounts (in cent)
#to add the two amounts
#to print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#Author: Emma Dunleavy

amount1 = int(input('Enter amount 1 (in cent):'))     #requests the user to inputs amount 1 as an integer
amount2 = int(input('Enter amount 2 (in cent):'))     #request the user to inputs amount 2 as an integer
print(str(amount1))                                 #prints inputted amount 1 as a string
print(str(amount2))                                 #prints inputted amount 2 as a string
amount1_converted=amount1/100                       #converts the inputted amount to cents by dividing by 100
amount2_converted=amount2/100
print(str(amount1_converted))                       #prints the converted amount
print(str(amount2_converted))
print(('The sum of these is €') + str(amount1_converted + amount2_converted)) #prints the total of the 2 amounts 