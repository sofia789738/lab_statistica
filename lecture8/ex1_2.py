#Write a program that, given a number N_max, generates N_toys toy experiments, 
#each containing a sample of N_max events following a chosen distribution, and calculates their mean.

#Add a histogram that visualizes the distribution of means across the toy experiments.

import random
import numpy as np
import matplotlib.pyplot as plt
from lib import mean

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def toy_esperiments (N_toys, N_max) :
    means = []
    for i in range (0, N_toys) :
        randlist = []
        for i in range (0, N_max) :
           randlist.append(random.random())
        my_mean = mean(np.array(randlist))
        means.append(my_mean)
    return means
   
def main () :
   #get the parameters
   n_toys = int(input('insert number of toy esperiments\n'))
   n_events = int(input('insert number of events for each esperiment\n'))
   #calculate the mean of n_toys toy esperiments
   means = toy_esperiments(n_toys, n_events)

   #plot the histogram
   xMin = min(means)
   xMax = max(means)
   n_bins = sturges (n_toys)
   bin_edges = np.linspace (xMin, xMax, n_bins)
   fig, ax = plt.subplots (nrows = 1, ncols = 1)
   ax.hist (means, bins = bin_edges, color = 'yellow')
   ax.set_title('means of toys esperiments')
   plt.show ()

   
if __name__ == "__main__" :
    main()
