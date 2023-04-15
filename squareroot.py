#this program takes a positive floating-point number as input and outputs an approximation of its square root
#Author: Emma Dunleavy

def sqrt(no, error=0.00000001):                     
    guess = no                                      # first guess is the number inputted
    diff = 99999999
    while diff > error:
        new_guess = guess - ((guess**2 - no) / (2*guess)) # Newtons method
        diff = new_guess - guess
        if diff < 0:
            diff *= -1                                     # to convert to an absolute value

        guess = new_guess                                  # update existing guess
    return guess

no=float(input("Please enter a positive number: "))  #to input a positive floating point number

print (f"The square root of {no} is appox.", (sqrt (no))) # to print approximate sq rt of original inputted value 



# reference: https://www.youtube.com/watch?v=tUFzOLDuvaE