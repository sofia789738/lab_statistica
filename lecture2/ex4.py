#Compare the time performances of element-wise operations performed between two lists with respect to the same operation performed in compact form between two NumPy arrays
import time 
import numpy as np 
import sys

def my_time(n) :

   list_a = list(range(n))
   list_b = list(range(n))
   a = np.array (list_a)
   b = np.array (list_b)
   
   time0_1 = time.time ()
   
   prod1 = [list_a[i] * list_b[i] for i in range (len (list_a))]
   time1 = time.time ()
   print ('time lists:', time1-time0_1, '\n')
   
   time0_2 = time.time ()
   prod2 = a * b
   time2 = time.time()
   print ('time arrays:', time2-time0_2, '\n')
  

def main () :
   my_time(int(sys.argv[1]))

if __name__ == "__main__" :
    main()
