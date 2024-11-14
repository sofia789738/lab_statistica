#Simulate a counting experiment with Poisson characteristics, 
#choosing a characteristic time t0 for a radioactive decay process and a measurement time tM for the counting window

#In a loop, simulate N pseudo-experiments of counting, where, for each of them, a sequence of random events is generated with an intertime characteristic of Poisson phenomena,
#until the total time elapsed is greater than the measurement time, counting the number of generated events that fall within the interval.

#Fill a histogram with the simulated counts for each experiment.

import random
import matplotlib.pyplot as plt
import numpy as np
from poisson_lib import exp_random

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main () :
    t0 = 5.
    tm = 7.
    tot = 500
    poisson = []
    for i in range (0,tot) :
       time = exp_random (t0)
       n = 0
       mean = 0.
       while time < tm :
          n = n+1
          time = time + exp_random (t0)  
       poisson.append(n)
    
    #print ('mean:', np.sum(poisson)/tot)

    #histogram
    xMin = min(poisson)
    xMax = max(poisson)
    n_bins = 8
    bin_edges = np.linspace (xMin, xMax, n_bins)

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (poisson, bins = bin_edges, color = 'blue')
    plt.show ()

if __name__ == "__main__" :
    main()