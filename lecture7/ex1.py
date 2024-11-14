#Generate a sample of pseudo-random numbers distributed according to an exponential density distribution with a characteristic time t0 of 5 seconds.
#Visualize the distribution of the obtained sample in a histogram using the inverse function method.

import random
import matplotlib.pyplot as plt
import numpy as np
import sys

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def inverse_exp (y, tau) :
    x = -tau*np.log(1-y)
    return x

def main () :
    tot = int((sys.argv[1]))
    tau = 5.
    randlist = []
    for i in range (0, tot) :
        randlist.append(inverse_exp (random.random(), tau))
    
    #to visualize the histogram
    xMin = min(randlist)
    xMax = max(randlist)
    n_bins = sturges(tot)
    bin_edges = np.linspace (xMin, xMax, n_bins)

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (randlist, bins = bin_edges, color = 'blue')
    plt.show ()

if __name__ == "__main__" :
    main()