#Use a function that generates random numbers according to the Poisson distribution, 
#with the mean expected events as an input parameter. (IN POISSON_LIB)

#drawing the probability density histogram.

#Calculate the sample statistics (mean, variance, skewness, kurtosis) from the input list using a library.

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson, kurtosis, skew
from poisson_lib import my_poissonian
from lib import mean, variance

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def main () :
    lambd = int(input('insert lambda\n'))
    poisson1 = my_poissonian(1000, lambd)
    poisson_v = np.array(poisson1)
    
    #sample statistics
    print('mean:', mean(poisson_v), '\nvariance:', variance(poisson_v),'\nskewness:', skew(poisson_v), '\nkurtosis:', kurtosis(poisson_v))

    #histogram
    xMin = min(poisson1)
    xMax = max(poisson1)
    n_bins = sturges(1000)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (poisson1, bins = bin_edges, color = 'blue')
    #overlay the poissonian pdf
    x = np.linspace(0, xMax, 100)
    plt.plot(x, poisson.pmf(x, lambd)*1000 , color='red')
    plt.show ()


if __name__ == "__main__" :
    main()

