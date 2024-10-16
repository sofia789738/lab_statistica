#Display the distributions of events from the two files of the previous exercises, overlaid, finding the best visualization for the comparison between the two histograms.

import matplotlib.pyplot as plt
import numpy as np

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main() :
   with open ('eventi_unif.txt') as input_file:
      sample1 = [float (x) for x in input_file.readlines()]
      N = len(sample1)
      xMin = min(sample1)
      xMax = max(sample1)
      
      with open ('eventi_gauss.txt') as input_file:
         sample2 = [float (x) for x in input_file.readlines()]
      
         fig, ax = plt.subplots (nrows=1, ncols=1)
         ax.hist (sample1, color = 'blue', alpha=0.5) 
         ax.hist (sample2, color = 'green', alpha=0.5) 
         ax.set_title ('overlaid histograms')
         n_bins = sturges(N)
         bin_edges = np.linspace (xMin, xMax, n_bins)
         
         plt.show ()
         
         
         
if __name__ == "__main__":
    main ()
