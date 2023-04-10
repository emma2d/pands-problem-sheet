#weekly task week 3 - modified
#program that reads in a >10 character account number 
#outputs the account number with only the last 4 digits showing (and the first digits replaced with Xs)
#author Emma Dunleavy


account_number=int(input('Please enter bank account number: '))

#converting account number to a string
str_account_number=str(account_number)

#replacing all but last for characters with x

encoded='x'*(len(str_account_number)-4) + str_account_number[-4:]

#printing encoded account number
print(encoded)

#assuming account number is >4 characters
#reference https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of