#Create one-dimensional NumPy arrays using different generation techniques

import numpy as np

def main() :
    list_one = [1,2,3,4,5]
    array_one = np.array (list_one)

    first = 1
    last = 6
    array_two = np.arange (first, last)

    print (array_one)
    print (array_two)
    
if __name__ == "__main__" :
    main()
