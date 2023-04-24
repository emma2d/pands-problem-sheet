#weekly task 07
# read in a text file from the command line and output the number of e's it contains
#Author Emma Dunleavy

import sys

filename = sys.argv[1]   # assuming the text file is the second arugment passed after the python 

print("filename", filename) #prints the inputed txt filename

with open(filename, 'r') as f:
    data = f.read()             #read content of file to string
    e_number = data.count('e')    #gets the number of occurances of the letter e within the text file read in
    E_number = data.count('E')
print("Number of lower case e's are", e_number, "and number of capital E's are", E_number)   #prints the string output and number of lower case e's and capital E's counted    


#Reference: https://www.youtube.com/watch?v=SJ2nWs4yl9k

