#Program that determines the solution of second-order equations
#Parameters of the equation put by the user on the command line

import sys
import math

def eq_2nd (a, b, c) :
    delta = b*b - 4*a*c
    
    if delta==0 :
        x = -(b/(2*a))
        print ('delta=0 : una soluzione doppia:', x)
        
    elif delta>0 :
        x_1 = (-b + math.sqrt(delta))/(2*a)
        x_2 = (-b - math.sqrt(delta))/(2*a)
        print ('delta>0 : due soluzioni:', x_1,',', x_2)
        
    else :
        print ('delta<0 : nessuna soluzione')
        
        
if len(sys.argv)<2 :
    print ('parametri mancanti')

else :  
    eq_2nd (float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

