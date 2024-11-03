#python library that implements the Fraction class, containing its constructor, 
#the data members to save numerator and denominator, and the class method that
#returns the division between the numerator and the denominator.

from math import gcd
class Fraction :

    #constructor of functions:
    def __init__(self, numerator, denominator) :

        if denominator == 0 :
          raise ValueError ('Denominator cannot be zero')
        if type(numerator) != int:
          raise TypeError ('Numerator must be an integer')
        if type(denominator) != int: 
          raise TypeError ('Denominator must be an integer')
        
        common_divisor = gcd (numerator, denominator)
        self.numerator = int(numerator / common_divisor)
        self.denominator = int(denominator / common_divisor)

   #methods to save the fraction and to calculate its float value
    def print (self) :
       print(self.numerator, '/', self.denominator)

    def division (self) :
       return float(self.numerator/self.denominator)
    
   #overloading of the +, -, *, / operations
   #(in such a way that each of them returns an object of the type Fraction)
    
    def __add__ (self, other) :
       new_n = self.numerator*other.denominator + other.numerator*self.denominator
       new_d = self.denominator*other.denominator
       return Fraction(new_n, new_d)
    
    def __sub__ (self, other) :
       new_n = self.numerator*other.denominator - other.numerator*self.denominator
       new_d = self.denominator*other.denominator
       return Fraction(new_n, new_d)
    
    def _mul_ (self, other) :
       new_n = self.numerator * other.numerator
       new_d = self.denominator * other.denominator
       return Fraction(new_n, new_d)
    
    def __div__ (self, other) :
       #check on the divider
       if other.numerator == 0 :
          print('the divider cannot be zero\n')
          exit
       #ratio of two functions
       new_n = self.numerator*other.denominator
       new_d = self.denominator*other.numerator
       return Fraction(new_n, new_d)
       

