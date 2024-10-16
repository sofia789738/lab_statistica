#function that, given the name of a text file containing a sample of events as input, is able to read the sample and save it in a numpy array, then calculate its mean, variance, standard deviation, standard deviation from the mean, display the sample in a histogram with an appropriately chosen definition range and bin number.  

#s string = name of the text
import matplotlib.pyplot as plt
import numpy as np
import math

def parameters (s) :
    with open (s) as input_file:
        sample_list = [float (x) for x in input_file.readlines()]
        sample_array = np.array (sample_list)   
        
        n = np.size(sample_array)
        tot = 0
        for i in range(0,n) :
           tot = tot + sample_array[i]
        mean = tot/n
        
        var = 0
        for i in range(0,n) :
           var = var + (pow((sample_array[i]-mean),2))
        variance= var/(n-1)
        
        std_dev = math.sqrt(variance)
        
        print('mean:', mean, '\nvariance:', variance, '\nstandard deviation:', std_dev)
        
        
#------------------------------------------------------------------

def hist(s) :
    with open (s) as input_file:
      sample = [float (x) for x in input_file.readlines()]
      xMin = min(sample)
      xMax = max(sample)
      n = len(sample)
      sturges = int(np.ceil( 1 + 3.322 * np.log(n)))
      fig, ax = plt.subplots (nrows=1, ncols=1)
      ax.hist (sample_hist, color = 'blue') 
      n_bins = sturges
      bin_edges = np.linspace (xMin, xMax, n_bins)
      
      plt.show ()

      
            

