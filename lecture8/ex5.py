#Implement the hit-or-miss integration method with the example function f(x) = sin(x).

#Write the algorithm that calculates the integral as function external to the main program, 
#ensuring it takes as input parameters the limits along the x and y axis, as well as the number of pseudo-random points to generate.

#Make sure the algorithm returns a container with two elements: the first element is the value of the integral, 
#the second is its uncertainty.

import random
import numpy as np

def f (x) :
    return np.sin(x) + 1.

#function to generate random points
def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x

#hit or miss algorithm
def HOM_integral (func, xmin, xmax, ymin, ymax, n_tot) :
    n_hit = 0
    for i in range (0, n_tot) :
        x = rand_range (xmin, xmax)
        y = rand_range (ymin, ymax)
        if (func(x) > y) :
             n_hit = n_hit + 1
    A = float((xmax-xmin) * (ymax-ymin))
    p = float (n_hit / n_tot)
    int = p * A
    int_unc = (A**2)/n_tot * p * (1-p)
    return int, int_unc
             

def main () :
    integral, uncertainty = HOM_integral(f, 0, 2*3.14, 0, 2, 1000)
    print ('value of the integral:', integral, '\nuncertainty on the integral:', uncertainty)


if __name__ == "__main__":
    main ()
