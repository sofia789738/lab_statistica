#write a program to draw the BINOMIAL DISTRIBUTION FUNCTION and its CUMULATIVE FUNCTION

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

def main () :
    n = 50
    prob = 0.4
    x = np.arange(n+1) #to count also zero
    y_1 = binom.pmf(x, n, prob)
    plt.plot(x, y_1, label="binomial_pmf")
    plt.savefig('binomial_pmf')

    plt.clf
    
    y_2 = binom.cdf(x, n, prob)
    plt.plot(x, y_2, label="binomial_cdf")
    plt.savefig('binomial_cdf')



if __name__ == "__main__":
    main ()