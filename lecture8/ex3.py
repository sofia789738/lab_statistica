#Compare the standard deviation of the mean calculated for each individual toy with the standard deviation of the sample of means

import random
import numpy as np
import matplotlib.pyplot as plt
from lib import mean, std_dev, std_dev_means

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def means_toy_esperiments (N_toys, N_max) :
    means = []
    for i in range (0, N_toys) :
        randlist = []
        for i in range (0, N_max) :
           randlist.append(random.random())
        my_mean = mean(np.array(randlist))
        means.append(my_mean)
    return means

def std_devs_toy_esperiments (N_toys, N_max) :
    std_devs = []
    for i in range (0, N_toys) :
        randlist = []
        for i in range (0, N_max) :
           randlist.append(random.random())
        my_std_dev = std_dev_means(np.array(randlist))
        std_devs.append(my_std_dev)
    return std_devs

def main () :
   #get the parameters
   n_toys = int(input('insert number of toy esperiments\n'))
   n_events = int(input('insert number of events for each esperiment\n'))

   #calculate the standard deviation of the sample of means
   means = means_toy_esperiments(n_toys, n_events)
   std_dev_sample = std_dev(np.array(means))
   std_deviations = std_devs_toy_esperiments (n_toys, n_events)

   #plot the results
   xMin = min(std_deviations)
   xMax = max(std_deviations)
   n_bins = sturges (n_toys)
   bin_edges = np.linspace (xMin, xMax, n_bins)
   fig, ax = plt.subplots (nrows = 1, ncols = 1)
   ax.hist (std_deviations, bins = bin_edges, color = 'yellow')
   ax.set_title('compare standard deviations')
   plt.axvline(x = std_dev_sample, color = 'black')
   plt.show ()

if __name__ == "__main__" :
   main()



