#Implement a pseudo-random number generator that uses the inverse function method to generate events
#distributed according to an exponential probability distribution.

#Visualize the distribution of the generated numbers

import random
import matplotlib.pyplot as plt
import sys
import numpy as np

#inverse of exp CDF
def inverse (y, lambd) :
    x = -1*np.log(1-y)/lambd
    return x

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main () :
    #parameters as input
    tot = int(sys.argv[1])
    tau = float (sys.argv[2])
    lambd = 1./tau

    #to generate random variables   
    randlist = []
    for i in range (0, tot) :
        randlist.append(inverse (random.random(), lambd))

    #to create the histogram
    xMin = min(randlist)
    xMax = max(randlist)
    n_bins = sturges(tot)
    bin_edges = np.linspace (xMin, xMax, n_bins)

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.set_title ('Histogram of random numbers', size=14)
    ax.set_xlabel ('random value')
    ax.set_ylabel ('events in bin')
    ax.hist (randlist, bins = bin_edges, color = 'blue')
    plt.savefig('Histogram of random numbers_inverse function algorithm')
    plt.show ()




if __name__ == "__main__" :
    main()