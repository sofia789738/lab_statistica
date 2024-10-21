#Implement a pseudo-random number generator according to a uniform distribution between two arbitrary endpoints.
#Visualize the distribution of the generated numbers.

import random
import matplotlib.pyplot as plt
import sys
import numpy as np

def rand_range (min, max, tot) :
    randlist = []
    for i in range (0,tot) :
         x = min + (max-min)*random.random()
         randlist.append (x)
    return randlist

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main () :
    tot = int (sys.argv[1])
    minv = int(input('select the min\n'))
    maxv = int(input('select the max\n'))
    sample = rand_range(minv, maxv, tot)
    print(sample)

    xMin = min(sample)
    xMax = max(sample)
    n_bins = sturges(tot)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges, color = 'blue')
    plt.show ()

    


if __name__ == "__main__" :
    main()



