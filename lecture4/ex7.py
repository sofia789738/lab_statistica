#Implement a pseudo-random number generator that uses the central limit theorem method 
#to generate events distributed according to a Gaussian probability distribution.

#Visually verify that as the number of events increases, the similarity between the obtained distribution and the Gaussian functional form increases, 
#both graphically and by using the moments of the distributions calculated on the generated event sample.

import random
import matplotlib.pyplot as plt
import numpy as np
from lib import median, mean, variance, std_dev

def TCL_random (seed, xmax, xmin, tot) :
    sum = seed
    for i in range (0, tot) :
        x = xmin + (xmax-xmin) * random.random()
        sum = sum + x
    average = sum / tot
    return average

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main() :
    #set parameters
    seed = 0
    xmax = float(input('insert max x\n'))
    xmin = float(input('insert min x\n'))
    tot = int(input('insert N (how many rv to calculate their average)\n'))
    n = int(input('how many rv to generate\n'))
    
    #generate n random variables
    randlist = []
    for i in range (0, n) :
        randlist.append(TCL_random(seed, xmax, xmin, tot))

    #print moments of the distribution
    d = np.array(randlist)
    print ('median:', median(d),'\n', 'mean:', mean(d),'\n', 'variance:', variance(d),'\n', 'standard deviation:', std_dev(d))

    #plot the histogram
    Min = min(randlist)
    Max = max(randlist)
    n_bins = sturges(tot)
    bin_edges = np.linspace (Min, Max, n_bins)

    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.set_title ('Histogram of random numbers', size=14)
    ax.set_xlabel ('random value')
    ax.set_ylabel ('events in bin')
    ax.hist (randlist, bins = bin_edges, color = 'blue')
    plt.show ()


if __name__ == "__main__" :
    main()