# After finding how the numpy.sort function works, write a Python library containing a function that determines the median of an array. Write a main program that tests the performance of the developed function.

import numpy as np
from lib import median 

def main () :

    #odd number of elements
    a_list = [1, 6, 8, 9, 56, 57, 45, 77, 98]
    a_array = np.array (a_list)
    print(median(a_array))
    #even number of elements
    b_list = [1, 6, 8, 9, 56, 57, 45, 77, 98, 11]
    b_array = np.array (b_list)
    print(median(b_array))
    
    
if __name__ == "__main__" :
    main()
  

