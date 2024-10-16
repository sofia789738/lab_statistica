

def function1 (x) :
   if x%2==0 or x%3==0 or x%5==0 or x%7==0 :
       return 0

def function2 (x, y) :
   if x%y==0 :
       return 0
      
      
      
if function1(int(input ('insert the first number\n')))==0 :
    print ('the number is divisible by 2, 3, 5, or 7')

dividend = int (input ('insert the dividend\n'))
divider = int (input ('insert the divider\n'))
if function2 (dividend, divider)==0 :
    print ('the number '+ str(dividend) + ' is divisible by ' + str(divider))
else :
    print ('the number '+ str(dividend) + ' is not divisible by ' + str(divider))
