#weekly task 07
# read in a text file from the command line and output the number of e's it contains
#Author Emma Dunleavy

import sys

filename = sys.argv[1]   # assuming the text file is the second arugment passed after the python 

print("filename", filename) #prints the inputed txt filename

with open(filename, 'r') as f:
    data = f.read()             #read content of file to string
    number = data.count('e')    #gets the number of occurances of the letter e within the text file read in
print(number)                   #prints the string output and number of e's counted    

#Reference: https://www.youtube.com/watch?v=SJ2nWs4yl9k

