#Implement a function that calculates the factorial of a number using a recursive function.

def factorial (n) :
    if n==1 or n==0 :
       return 1
    else :
       return n*factorial(n-1)
      
def main () :
    n = int(input ('insert integer number\n'))
    print ('the factorial of', n , 'is:', factorial(n))

if __name__ == "__main__" :
    main()