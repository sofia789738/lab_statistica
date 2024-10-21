#Implement a pseudo-random number generator that uses the inverse function method to generate events
#distributed according to an exponential probability distribution.

#Visualize the distribution of the generated numbers

import random
import matplotlib.pyplot as plt
import sys
import numpy as np
import scipy.stats as st

def main () :
    tot = int(sys.argv[i])
    x = np.linspace (-200, 200., 100)
    pdf = st.expon.pdf(x, loc=0, scale=1)
    F = np.log(pdf)
    randlist_y = []
    for i in range (0, tot) :
        yi = random.random ()
        if yi = 
           randlist_y.append (yi)
    for i in range (0, tot) :
        x_i = st.expon.pdf(F, loc=0, scale=1)
        randlist.append(x_i)
        







if __name__ == "__main__" :
    main()