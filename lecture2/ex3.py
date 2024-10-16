#Create a one-dimensional array containing the sequence of the first 50 even natural numbers

import numpy as np

def main() :
    array_50 = np.arange (1,51)
    
    even = [2]
    odd = [1]
    for i in range (2,50) :
        if array_50[i]%2==0 :
            even.append(array_50[i])
        else :
            odd.append(array_50[i])
            
    array_even = np.array (even)
    array_odd = np.array (odd)
    print (array_even, '\n', array_odd)
    
    
if __name__ == "__main__" :
    main()    

            
