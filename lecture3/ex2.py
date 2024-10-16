#from a text file print the first 10 positive elements to the screen, count the number of events, determinate the minimum and the maximum value

import matplotlib.pyplot as plt
import numpy as np

def main () :
   with open ('eventi_unif.txt') as input_file:
      sample = [float (x) for x in input_file.readlines()]
      positivi = [x for x in sample if x>0]
      
      print (positivi[:10])
      
      tot = len(sample)
      print ('the number of events is:', tot,'\n')
      
      mini = min(sample)
      maxi = max(sample)
      print('the minimum element is',  mini, '\nthe maximum element is', maxi)
       
            
   
   
   
  
   
  
if __name__ == "__main__":
    main ()
