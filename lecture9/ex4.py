#Write a function likelihood that calculates the likelihood as the parameter t0 varies, 
#for a sample of pseudo-random events generated according to an exponential function.

import random
import numpy as np
import scipy.stats as st

def exp_pdf (x, t0) :
    #exponential probability density function
    if t0 == 0. : 
        return 1.
    return (np.exp (-1 * x / t0)) / t0

def generate_exp (n_tot, t0) :
    exp_randlist = []
    for i in range (0, n_tot) : 
        y = random.random()
        x = -t0 * np.log(1-y)
        exp_randlist.append(x)
    return exp_randlist

#likelihood function calculated for a sample according to their pdf with parameter t0
def likelihood (randlist, pdf, t0) :
    L = 1.
    sample = np.array (randlist)
    for x in sample :
        L = L * pdf (x, t0)
    return L

def main () :
    #generate random numbers
    N = int(input('how many numbers to generate\n'))
    t0 = float(input('insert tau\n'))
    randlist = generate_exp (N, t0)
    #get the likelihood
    y = likelihood (randlist, exp_pdf, t0)
    print ('likelihood for t0 =', t0, ':\n', y)

if __name__ == "__main__":
    main ()