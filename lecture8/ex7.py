#Implement the crude-MC integration method with the example function f(x) = sin(x) +1.

#Write the algorithm that calculates the integral as a function external to the main program, 
#ensuring it takes as input parameters the limits along the x axis and the number of pseudo-random points to generate.

#Make sure the algorithm returns a container with two elements: 
#the first element is the value of the integral, the second is its uncertainty.

import random
import numpy as np

def f (x) :
    return np.sin(x) + 1.

#function to generate random points
def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x

def MC_integral (func, xmin, xmax, n_tot) :
    sum = 0.
    sum_var = 0.
    for i in range (0, n_tot) :
        x = rand_range (xmin, xmax)
        y = func (x)
        sum = sum + y
        sum_var = sum_var + y**2
    mean = sum / float (n_tot) #E(func(x))
    var_biased = sum_var / float (n_tot) - mean**2 #V biased beacuse the true value of the mean is unknown
    var_unbiased = var_biased * (float(n_tot)-1) / float(n_tot) #V(func(x))
    integral = (xmax - xmin) * mean
    uncertainty = (xmax - xmin) * np.sqrt(var_unbiased / float(n_tot))
    return integral, uncertainty

def main () :
    integral, uncertainty = MC_integral(f, 0, 2*3.14, 1000)
    print ('value of the integral:', integral, '\nuncertainty on the integral:', uncertainty)

if __name__ == "__main__":
    main ()

