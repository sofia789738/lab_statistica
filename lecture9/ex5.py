#Write a function loglikelihood that calculates the logarithm of the likelihood as the parameter t0 varies, 
#for a sample of pseudo-random events generated according to an exponential function.

import random
import numpy as np

def exp_pdf (x, t0) :
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

#log-likelihood function calculated for a sample according to their pdf with parameter t0
def log_likelihood (lik, randlist, pdf, t0) :
    l = 0.
    sample = np.array (randlist)
    L = lik (randlist, pdf, t0)
    if L <= 0 : #the logarithm of the likelihood is defined only when the likelihood is strictly positive
        return 0
    else :
       for x in sample :
          l = l + np.log (pdf (x, t0))
       return -l 

def main () :
    #generate random numbers
    N = int(input('how many numbers to generate\n'))
    t0 = float(input('insert tau\n'))
    randlist = generate_exp (N, t0)
    #get the log-likelihood
    y = log_likelihood (likelihood, randlist, exp_pdf, t0)
    print ('log-likelihood for t0 =', t0, ':\n', y)

if __name__ == "__main__":
    main ()