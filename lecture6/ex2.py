#Determine the zero of the function g(x) = cos(x) using the bisection method in the interval (0, 4) using a recursive function

import numpy as np

def recursive_bisection (xmin, xmax, g, prec=0.0001) :
    av = (xmin+xmax)/2
    if (xmax-xmin)<prec :
       return av
    if g(xmin) * g(av) > 0. :
       return recursive_bisection (av, xmax, g, prec=0.0001)
    else :
       return recursive_bisection (xmin, av, g, prec=0.0001)
    

def main() :
    x = np.linspace (-10, 10, 100)
    print('the zero is:', recursive_bisection (0, 4, lambda x : np.cos(x), prec=0.0001))
    
if __name__ == "__main__" :
    main()