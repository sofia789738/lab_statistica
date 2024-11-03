#Write a python program that reads the sample file and, using the map function, 
#creates the distribution of the squares and cubes of random Gaussian numbers, 
#respectively, using lambda functions in the process.

#Plot the distribution of them, together with the original sample one, all in the same frame.

import matplotlib.pyplot as plt
import numpy as np
import sys

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main () :
    with open ('eventi_gauss.txt') as input_file:
      sample = [float (x) for x in input_file.readlines()]
      
      #use of map
      squares = list(map(lambda x : x**2, sample))
      cubes = list(map(lambda x : x**3, sample))
      
      #plotting the distribution
      xMin = min(sample)
      xMax = max(sample)
      N = len(sample)
      
      fig, ax = plt.subplots (nrows=1, ncols=1)
      n_bins = sturges(N)
      bin_edges = np.linspace (xMin, xMax, n_bins)
      ax.hist(sample, bins=bin_edges, color = 'blue', alpha=0.5) 
      ax.hist(squares, bins=bin_edges, color = 'red', alpha=0.5) 
      ax.hist(cubes, bins=bin_edges, color = 'orange', alpha=0.5) 
      ax.set_title('Histogram example', size=14)
      
      plt.show ()


if __name__ == "__main__":
    main ()