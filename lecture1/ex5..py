import sys
from ex3 import Fibonacci

    
#A function that creates a new list which contains only elements with even index of the Fibonacci sequece
#Args:list:a list with the Fibonacci sequence
#Returns:list:a list with the lements with even index of the arg
def even(mylist) :
    even_list = [1]
    i=1
    while i<len(mylist) :
          if i%2==0 :
                even_list.append(mylist[i])
          i=i+1
    return even_list
          
#A function that creates a new list which contains only elements with odd index of the Fibonacci sequece
#Args:list:a list with the Fibonacci sequence
#Returns:list:a list with the lements with odd index of the arg         
def odd(mylist) :
    odd_list = [1]
    i=2
    while i<len(mylist) :
          if i%2!=0 :
                odd_list.append(mylist[i])
          i=i+1
    return odd_list
             
   

Fib = Fibonacci(int(sys.argv[1]))

print (even(Fib))
print (odd(Fib))

