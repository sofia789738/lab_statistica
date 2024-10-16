#program that finds the list of prime integer numbers smaller than 100, starting by knowing that 2 is a prime number

import sys

def prime(n) :
    list_prime = [2]
    dividers = [2]
    
    for i in range(3,n) :
        dividers.append(i)
        aux=0
        for j in range(0,i-2) :
            if i % dividers[j] != 0 :
                aux = aux+1
                if aux == i-2 :
                    list_prime.append(i)
                
                
    return list_prime
               
               
print (prime(100))
