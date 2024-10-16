import sys

def Fibonacci(n) :
    Fib = [1,1]
    i=0
    j=0
    k=1
    while i<n :
         Fib.append((Fib[j]+Fib[k]))
         j=j+1
         k=k+1 
         i=len(Fib)
    return Fib
         
print (Fibonacci(int(sys.argv[1])))
