# collatz.py is a program that asks the user to input any positive integer 
# outputs the successive values of the following calculation
#At each step calculate the next value by taking the current value and
#if it is even, divide it by two
#if it is odd, multiply it by three and add one

#Author: Emma Dunleavy


pos_int = int(input("Enter a positive integer:"))
pos_ints=[pos_int] #pos_int will create a list

while pos_int >1:                         # while inputted positive integer is > 1
    if pos_int % 2 == 0:                  # if it is an even number
        pos_int = pos_int/2               # it is divided by 2
        pos_ints.append(int(pos_int)) 

    else:
        pos_int % 2 !=0                  # or else if it is an odd number
        pos_int = (pos_int * 3) + 1      # multiply by 3 and add 1
        pos_ints.append(int(pos_int))


       
print(pos_ints)                            # print the list of numbers generated


#reference : https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php