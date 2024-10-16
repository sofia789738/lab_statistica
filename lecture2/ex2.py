# Create a one-dimentional NumPy array containing a sequence of integer numbers from 1 to 100. Starting from this, create a one-dimensional NumPy array containing in each entry the sum of integer numbers from 1 until the index of that entry


import numpy as np

def main() :
    first = 1
    last = 101
    array_100 = np.arange (first, last)
    
    array_sum = np.empty
    array_sum = np.cumsum(array_100)
    print (array_100, '\n')
    print (array_sum)


if __name__ == "__main__" :
    main()
