import random
import numpy as np

#functions to generate events according to an exponential density distribution (inverse method function)
def exp_random_list (tot, tau) :
    randlist = []
    for i in range (0, tot) :
        randlist.append(-tau*np.log(1-random.random()))
    return randlist

def exp_random (tau) :
    return -tau*np.log(1-random.random())

#function that generates random numbers according to the Poisson distribution, with the mean expected events as an input parameter

def my_poissonian_1p (tot, lambd) :
    t0 = 1 #fixed
    tm = t0*lambd #measurement time tM for the counting window
    poisson = []
    for i in range (0, tot) :
       time = exp_random (t0)
       n = 0
       while time < tm : 
          n = n+1
          time = time + exp_random (t0)  
       poisson.append(n)

    return poisson

def my_poissonian_2p (tot, t0, tm) :
    poisson = []
    time = exp_random (t0)
    n = 0
    for i in range (0, tot) :
        while time < tm :
            n = n+1
            time = time + exp_random (t0)
        poisson.append(n)

    return poisson
