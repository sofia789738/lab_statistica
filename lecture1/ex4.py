import sys

def Fibonacci(n) :
    Fib = {1:1, 2:1}
    n_1=1
    n_2=1
    for k in range(3,n) :
         aux=n_2
         n_2=n_1+n_2
         n_1=aux
         Fib[k+1] = n_2
       
    return Fib
         
print (Fibonacci(int(sys.argv[1])))
