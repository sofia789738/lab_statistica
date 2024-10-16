#create a one-dimensional histogram filled with 5 values and save the histogram image to a png file

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
 
 
def main() :
    sample = [2, 2.5, 3, 4, 2]
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.hist (sample, color = 'red')
    plt.show ()
    plt.savefig('hystogram.png')
 
 
 

 
if __name__ == "__main__":
    main ()
