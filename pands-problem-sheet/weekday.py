#this program outputs whether or not today is a weekday

#Author: Emma Dunleavy

from datetime import date

today=date.today()                  #to get today's date

print ("today's date is:", today)   #to print out today's date

#ref https://www.programiz.com/python-programming/datetime/current-datetime

no = today.weekday()                #to assign each day of the week a number 0 for Monday, 1 for Tesday ...6 for Sunday

if no < 5:                          # if less than 5 ie Monday to Friday
    print("Yes, unfortunately today is a week day")
else:                               #5 Sat, 6 Sun
    print("It's the weekend, yeh!")

#ref https://pynative.com/python-get-the-day-of-week/
