#weekly task week 3
#program that reads in a 10 character account number 
#outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
#author Emma Dunleavy


account_number=int(input('Please enter a 10 digit account number: '))

#converting account number to a string
str_account_number=str(account_number)

#printing first 6 characters as "X" and last 4 characters of account number
encoded=("XXXXXX" + str_account_number[6:])
#printing encoded account number
print(encoded)
#reference https://www.w3schools.com/python/python_strings_slicing.asp
