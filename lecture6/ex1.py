#Determine the zero of the function g(x) = cos(x) using the bisection method in the interval (0, 4)

import numpy as np

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
    
def main() :
    x = np.linspace (-10, 10, 100)
    print('the zero is:', bisection (0, 4, lambda x : np.cos(x), prec=0.0001))
    

if __name__ == "__main__" :
    main()