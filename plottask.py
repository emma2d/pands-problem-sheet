#week08 task, a program that displays
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#Author: Emma Dunleavy

import matplotlib.pyplot as plt
import numpy as np


mean=5                  #assign value of mean
std=2                   #assign value of standard deviation
number_values=1000      #assign number of values to be displayed

values=np.random.normal(mean, std, number_values)   #normal distribution of values as per previously defined 
print(values)                                       #print 1000 random values

plt.hist(values)                                    #plot the histogram of the 1000 random values generated
plt.xlim(right=12, left=-2)                         #set the x axis range as -2 to 12
plt.ylim(top=1000, bottom =0)                       #set the y axis range as 0 to 1000
plt.show()                                          #displays the plot


# a plot of the function  h(x)=x cubed in the range [0, 10] on the one set of axes

def h(x):                           #define function h(X)
    return x**3                     # return x cubed

xpoints=np.arange(0, 11)            #assign range 1-10
ypoints=h(xpoints)                  # get the cube of the range

plt.plot(xpoints, ypoints, color='b', label="h(x)")
plt.xlabel('xlabel')                            #label x axis 
plt.ylabel('ylabel')                            #label y axis
plt.title('Plotting Example')                   #label graph
plt.xlim(right=12, left=-2)                     #set the x axis range as -2 to 12
plt.ylim(top=1000, bottom =0)                   #set the y axis range as 0 to 1000
plt.legend()                                    #add legend
plt.show()                                      #display the plot