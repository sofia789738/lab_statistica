#test function of the class inside the library file itself, that verifies the output of each method of the class, 
#and that prints on screen the value of the numerator and of the denominator of a fraction.

import fraction_lib

def main() :
    n = int(input('insert the numerator\n'))
    d = int(input('insert the denominator\n'))
    my_fraction = fraction_lib.Fraction (n,d)
    print('numerator:', my_fraction.numerator)
    print('denominator:', my_fraction.denominator)
    print('ratio:', my_fraction.division())
         
if __name__ == "__main__":
    main ()
    