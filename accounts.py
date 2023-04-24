#weekly task week 3
#program that reads in a 10 character account number 
#outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
#author Emma Dunleavy

account_number=int(input('Please enter a 10 didit bank account number: '))

#converting account number to a string
str_account_number=str(account_number)

while len((str_account_number)) != 10: #while the length of the bank account inputted does not equal 10
    account_number=int(input('Please enter a 10 didit bank account number: ')) #repeat request to input 10 didits
    str_account_number=str(account_number)  # convert to string again

#replacing all but last for characters with x

encoded='x'*(len(str_account_number)-4) + str_account_number[-4:]

#printing encoded account number
print(encoded)

#reference https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of
#reference https://www.w3schools.com/python/python_strings_slicing.asp