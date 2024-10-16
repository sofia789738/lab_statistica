#calculate mean, variance, standard deviation

import matplotlib.pyplot as plt
import numpy as np
import math

def main() :
    with open ('eventi_unif.txt') as input_file:
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

         
if __name__ == "__main__":
    main ()
