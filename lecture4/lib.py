import numpy as np
import math


#determinate the median of an array
def median (my_array) :
    array_s = np.sort(my_array, axis=None)
    l = np.size(array_s)
     
    if l%2!=0 :
        i = int((l-1)/2)
        m = array_s[i]
    else :
        i = int(l/2 - 1)
        j = int(i + 1)
        m = (array_s[i] + array_s[j])/2
        
    return m
#_____________________________________________________________________

#given an array, determinate the value below which lies the 25% of the values
def below25 (my_array) :
    array_s = np.sort(my_array, axis=None)
    l = np.size(array_s)
    i = int(l/4)
    v = array_s[i]
    return v
    
#given an array, determinate the value above which lies the 25% of the values
def above25 (my_array) :
    array_s = np.sort(my_array, axis=None)
    l = np.size(array_s)
    i = int((3*l)/4)
    v = array_s[i]
    return v
    
#_____________________________________________________________________
   
#given an array, determinate the value below which lies the N% of the values
def belowN (my_array, N) :
    array_s = np.sort(my_array, axis=None)
    l = np.size(array_s)
    i = int((l*N)/100)
    v = array_s[i]
    return v

#given an array, determinate the value above which lies the N% of the values
def aboveN (my_array,N) :
    array_s = np.sort(my_array, axis=None)
    l = np.size(array_s)
    i = int((N*l)/100)
    v = array_s[i]
    return v
    
#___________________________________________________________________

#given an array calculate the mean of its elements
def mean (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    
    m = tot/n
    return m
    
#given an array calculate the variance of its elements
def variance (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    m = tot/n
    
    var = 0
    for i in range(0,n) :
        var = var + (pow((my_array[i]-m),2))
    variance= var/(n-1)
    return variance

#given an array calculate the standard deviation of its elements
def std_dev (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    m = tot/n
    
    var = 0
    for i in range(0,n) :
        var = var + (pow((my_array[i]-m),2))
    variance= var/(n-1)
    std_dev = math.sqrt(variance)
    return std_dev
    
   
