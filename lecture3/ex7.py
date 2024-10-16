#draw a Gaussian distribution and its cumulative function

import matplotlib.pyplot as plt
import numpy as np
import math

def Gaussian (x, mean, sigma) :
    return np.exp (-0.5 * pow ((x - mean) / sigma, 2.)) / (math.sqrt((2 * np.pi) * sigma))
    

def main() :
   
    x_coord = np.linspace (-3., 3., 10000)
    y_coord = np.arange (0., x_coord.size)
    
    for i in range (x_coord.size):
        y_coord[i] = Gaussian (x_coord[i], 0., 1.)
        
    fig, ax = plt.subplots (nrows = 1, ncols = 1)    
        
    ax.plot(x_coord, y_coord, label='PDF')
    ax.set_title ('pdf')
    ax.set_xlabel ('x')
    ax.set_ylabel ('f(x)')
    
   
    plt.savefig ('PDF_3.7')   
    
    
    
if __name__ == "__main__":
    main ()
    
    
