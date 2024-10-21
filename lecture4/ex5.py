#Implement a pseudo-random number generator that uses the try-and-catch method to generate pseudo-random 
#numbers according to an arbitrary probability distribution (Take the probability density function (pdf) as an input parameter)
#Visualize the distribution of the generated numbers.

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import sys

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))


def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x

def rand_TAC (xmin, xmax, ymax,) :
    x = rand_range (xmin, xmax)
    y = rand_range (0, ymax)
    while (y > norm.pdf(x, 100., 5.)) :
     x = rand_range (xmin, xmax)
     y = rand_range (0, ymax)
    return x

def main () :
    N = int(sys.argv[1])
    norm_fix = norm(100., 5.)
    x = np.linspace (50., 150., 100)
    pdf = norm_fix.pdf(x)
    ymax = max(pdf)
    sample = []
    for i in range (0, N) :
        sample.append(rand_TAC(90, 110, ymax))
    print (sample)

    xMin = min(sample)
    xMax = max(sample)
    n_bins = sturges(N)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges, color = 'blue')
    plt.show ()



if __name__ == "__main__":
    main ()
