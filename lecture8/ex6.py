#Insert the calculation of the integral with HOM alg into a loop that, as the number N of generated points varies, 
#displays the value of the integral and its uncertainty.

#Use a scatter plot to visualize the trends of the integral value and its uncertainty as N varies on a logarithmic scale.

import random
import numpy as np
import matplotlib.pyplot as plt

def f (x) :
    return np.sin(x) + 1.

#function to generate random points
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

def main () :
    N_min = int(input('insert minimum number of points to generate\n'))
    N_max = int(input('insert maximum number of points to generate\n'))
    N = []
    v_integral = []
    v_uncertainty = []

    #calculation of the integral and its uncertainty in a loop that collects the results in lists
    while (N_min < N_max) :
        integral, uncertainty = HOM_integral (f, 0, 2*3.14, 0, 2, N_min) #extremes for f = sin(x) + 1
        v_integral.append(integral)
        v_uncertainty.append(uncertainty)
        N.append(N_min)
        print ('value of the integral:', integral, '\nuncertainty on the integral:', uncertainty, '\n')
        N_min = N_min * 5
 
    #scatter plot of the results 
    x = np.array (N) 
    y = np.array (v_integral)
    plt.errorbar(x, y, xerr = 0., yerr = v_uncertainty, color = 'red')
    plt.title ('integral value and its uncertainty as N varies')
    plt.xlabel ('number of points generated')
    plt.ylabel ('integral')
    plt.show()


if __name__ == "__main__":
    main ()