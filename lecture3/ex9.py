#Use the Python `scipy.stat.norm` object to determine the area of a normal distribution 
#of its tails outside the range included within an interval of 1, 2, 3, 4, and 5 
#standard deviations around its mean

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def main() :
    norm_fix = norm(0., 1.)
    for sigma in range (1,6) :
        area = norm_fix.cdf(0. - sigma) + 1. -norm_fix.cdf(0. + sigma)
        
        print('the area outside a range of', sigma, 'sigmas is', area)



         
if __name__ == "__main__":
    main ()