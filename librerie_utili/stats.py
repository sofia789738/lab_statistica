import numpy as np
import math
from scipy.stats import kurtosis, skew

#mediana di un vettore
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
#media di un vettore
def mean (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    m = tot/n
    return m
#___________________________________________________________________
#varianza di un vettore
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
#___________________________________________________________________
#deviazione standard di un vettore
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
#___________________________________________________________________
#deviazione standard di un vettore nota la media
def std_dev_mean (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    m = tot/n
    var = 0
    for i in range(0,n) :
        var = var + (pow((my_array[i]-m),2))
    variance= var/(n-1)
    std_dev_mean = math.sqrt(variance/n)
    return std_dev_mean
#___________________________________________________________________
#skewness di un vettore
def skewness (my_array) :
    return skew(my_array)
#___________________________________________________________________
#kurtosis di un vettore
def my_kurtosis (my_array) :
    return (kurtosis(my_array))
#_____________________________________________________________________________________________________________________

#dato un file di testo s contenente un sample di eventi, leggere s, salvarne i dati in un array e calcolarne i momenti   
#media, varianza, deviazione standard, deviazione standard dalla media
def moments (s) :
    with open (s) as input_file:
        sample_list = [float (x) for x in input_file.readlines()]
        sample_array = np.array (sample_list)   
        
        n = np.size(sample_array)
        tot = 0
        for i in range(0,n) :
           tot = tot + sample_array[i]
        mean = tot/n
        
        var = 0
        for i in range(0,n) :
           var = var + (pow((sample_array[i]-mean),2))
        variance= var/(n-1)
        
        std_dev = math.sqrt(variance)

        std_dev_mean = math.sqrt (variance / n)
        
        print('mean:', mean, '\nvariance:', variance, '\nstandard deviation:', std_dev, '\nstandard deviation from the mean:', std_dev_mean)