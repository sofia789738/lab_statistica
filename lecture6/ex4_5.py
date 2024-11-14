#Determine the minimum of the function g(x) = x2 + 7.3x + 4 using the golden ratio search method in the interval (-10, 10)

import numpy as np
import matplotlib.pyplot as plt
import math

#using a loop
def golden_ratio (xmin, xmax, g, prec=0.001):
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    
    while (xmax-xmin) > prec :
        if g(xi) > g (xf) :
           xmin = xi
           xi = xf
           xf = xmin + r*(xmax-xmin)
        else :
           xmax = xf
           xf = xi
           xi = xmin + (1-r)*(xmax-xmin)
           
    return (xmax+xmin)/2
    
#using a recursive function
def rec_golden_ratio (xmin, xmax, g, prec=0.001):
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    
    if xmax-xmin < prec :
        return (xmax+xmin)/2
    
    if g(xi) > g (xf) :
        return rec_golden_ratio(xi, xmax, g, prec=0.001)
    else :
        return rec_golden_ratio(xmin, xf, g, prec=0.001)
    
def g (x) :
    return x*x +7.3*x+4
    
def main () :
    x = np.linspace (-10, 10, 100)
    plt.plot(x, g(x), label="function")
    #plt.show()

    print ('the minimum of the function (using a loop) is:', golden_ratio (-10, 10, g, prec=0.001), '\n')
    print ('the minimum of the function (using a recursive function) is:', rec_golden_ratio (-10, 10, g, prec=0.001))
    
    
if __name__ == "__main__" :
    main()