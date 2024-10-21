# Fill a histogram with the first N numbers contained in the file, where N is a command-line parameter during program execution.
# Choose the histogram’s definition range and its bin number based on the numbers to be represented.

import matplotlib.pyplot as plt
import numpy as np
import sys

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))


def histogram (N) :
   with open ('eventi_gauss.txt') as input_file:
      sample = [float (x) for x in input_file.readlines()]
      sample_hist = sample[:N]
      xMin = min(sample_hist)
      xMax = max(sample_hist)
      
      fig, ax = plt.subplots (nrows=1, ncols=1)
      ax.hist (sample_hist, color = 'blue') 
      n_bins = sturges(N)
      bin_edges = np.linspace (xMin, xMax, n_bins)
      plt.savefig('histogram3')

      plt.show ()
      

histogram(int(sys.argv[1]))
