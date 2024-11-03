#Write a python program that reads the sample file and, using the filter function, 
#creates two different sub-sets of events containing those larger or smaller than the average respectively, 
#using lambda functions in the process.

#Show that the sigma of the two subsets is half the one of the parent sample.

import numpy as np
import math

def mean (v) :
    n = np.size(v)
    tot = 0
    for i in range(0,n) :
       tot = tot + v[i]
    return (tot/n)

def variance (v, mean) :
   var = 0
   n = np.size(v)
   for i in range(0,n) :
      var = var + (pow((v[i]-mean),2))
   return (var/(n-1))

def main () :
    with open ('eventi_unif.txt') as input_file:
      sample_list = [float (x) for x in input_file.readlines()]
      sample_array = np.array (sample_list)   

      #get paramaters of the whole input file 
      M = mean(sample_array)
      V = variance(sample_array, M)
      sigma = math.sqrt(V)

      #use of filter and creations of two subsets
      larger = list (filter(lambda x: x-M >= 0, sample_list))
      smaller = list (filter(lambda x: x-M <= 0, sample_list))
      
      #compare sigmas of the subsets and of the parent sample
      larger_array = np.array(larger)
      smaller_array = np.array(smaller)
      Ml = mean(larger_array)
      Ms = mean(smaller_array)
      Vl = variance(larger_array, Ml)
      Vs = variance(smaller_array, Ms)
      sigmal = math.sqrt(Vl)
      sigmas = math.sqrt(Vs)
     
      #print the results
      print('the sigma of the main sample is:', sigma, '\nthe sigmas of the subsets are:', sigmal, sigmas)



if __name__ == "__main__":
    main ()



