#Use the hit-or-miss method to estimate the integral underlying a Gaussian probability distribution
#with μ=0 and σ=1 within a generic interval [a,b].

#Calculate the integral contained within the intervals [-kσ, kσ] as k varies from 1 to 5.

import random
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def f (x) :
    norm_fix = norm(0., 1.)
    return norm_fix.pdf(x)

def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x

def HOM_integral (func, xmin, xmax, ymin, ymax, n_tot) :
    n_hit = 0
    for i in range (0,n_tot) :
        x = rand_range (xmin, xmax)
        y = rand_range (ymin, ymax)
        if (func(x) > y) :
             n_hit = n_hit + 1
    A = float((xmax-xmin) * (ymax-ymin))
    p = float (n_hit / n_tot)
    int = p * A
    int_unc = (A**2)/n_tot * p * (1-p)
    return int, int_unc

def main() :
     #calculate the integral within a generic interval 
     a = float (input('insert x_min\n'))
     b = float (input('insert x_max\n'))
     N = int (input('insert number of random points to generate\n'))
     integral, uncertainty = HOM_integral (f, a, b, 0, 1, N)
     print ('value of the integral of Gaussian pdf:', integral, '\nuncertainty on the integral:', uncertainty, '\n')
     print ('----------------------------------------------------------------')

     #calculate the integral within a simmetrical interval 
     for i in range (1, 5) :
          x_min = -i
          x_max = i
          integral, uncertainty = HOM_integral (f, x_min, x_max, 0, 1, N)
          print ('integral in a range of', i, 'sigmas\n')
          print ('value of the integral:', integral, '\nuncertainty on the integral:', uncertainty, '\n')
          print ('-----------------------------------------------------------------')






if __name__ == "__main__":
    main ()

    
    