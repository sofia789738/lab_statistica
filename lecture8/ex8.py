#Insert the calculation of the integral with crude MC alg into a loop that, 
#as the number N of generated points varies, displays the value of the integral and its uncertainty.

#Plot the trends of the integral value and its uncertainty as N varies on a logarithmic scale.

import random
import numpy as np
import matplotlib.pyplot as plt

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
    N_min = int(input('insert minimum number of points to generate\n'))
    N_max = int(input('insert maximum number of points to generate\n'))
    N = []
    v_integral = []
    v_uncertainty = []

    #calculation of the integral and its uncertainty in a loop that collects the results in lists
    while (N_min < N_max) :
        integral, uncertainty = MC_integral (f, 0, 2*3.14, N_min) 
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
