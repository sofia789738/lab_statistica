import numpy as np
import time

def bisection (xmin, xmax, g, prec=0.0001) :
    av = xmin
    while (xmax-xmin > prec) :
        av = (xmax+xmin)/2
        fmedia = g(av)
        if fmedia == 0 :
            return av
        if g(xmin) * fmedia > 0. :
            xmin = av 
        else :
            xmax = av
    return av
    
def recursive_bisection (xmin, xmax, g, prec=0.0001) :
    av = (xmin+xmax)/2
    if (xmax-xmin) < prec :
       return av
    if g(xmin) * g(av) > 0. :
       return recursive_bisection (av, xmax, g, prec=0.0001)
    else :
       return recursive_bisection (xmin, av, g, prec=0.0001)
    
    
def main() :
    x = np.linspace (-10, 10, 100)
    
    t0_loop = time.time()
    bisection (0, 4, lambda x : np.cos(x), prec=0.0001)
    t1_loop = time.time()
    print ('time of bisection method:', (t1_loop-t0_loop))
    
    t0_recursive = time.time()
    recursive_bisection (0, 4, lambda x : np.cos(x), prec=0.0001)
    t1_recursive = time.time()
    print ('time of recursive bisection method:', (t1_recursive-t0_recursive))
    

if __name__ == "__main__" :
    main()