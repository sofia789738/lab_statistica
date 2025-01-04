#Write a program that plots the exponential probability distribution with a fixed parameter t0.

import random
import matplotlib.pyplot as plt
import numpy as np

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def generate_exp (n_tot, tau) :
    exp_randlist = []
    for i in range (0, n_tot) : 
        y = random.random()
        x = -tau * np.log(1-y)
        exp_randlist.append(x)
    return exp_randlist

def main () :
    #generate random numbers
    N = int(input('how many numbers to generate\n'))
    tau = 5. #fixed
    randlist = generate_exp(N, tau)

    #plot the random numbers in a histogram
    xMin = min(randlist)
    xMax = max(randlist)
    n_bins = sturges(N)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.hist (randlist, bins = bin_edges, color = 'yellow')
    ax.set_title ('random numbers distributed according to an exponential function')
    plt.show()

   
if __name__ == "__main__" :
    main()


