#Determine the maximum of a given function (g) in a fixed interval using the golden ratio search method

import numpy as np
import matplotlib.pyplot as plt
import math

def golden_ratio_max(xmax, xmin, g, prec=0.001) :
    r = (math.sqrt(5)-1)/2
    xf = 0.
    xi = 0.
    
    while (xmax-xmin) > prec :
        xf = xmin + r*(xmax-xmin)
        xi = xmin + (1-r)*(xmax-xmin)

        if g(xf) > g (xi) :
           xmin = xi
        else :
           xmax = xf
           
    return (xmax+xmin)/2.

def g (x) :
    return -(x*x +7.3*x+4)
    
def main () :
    x = np.linspace (-10, 10, 100)
    plt.plot(x, g(x), label="function")
    #plt.show()
    print ('the maximum of the function is:', golden_ratio_max (-10, 10, g, prec=0.001))
      
if __name__ == "__main__" :
    main()