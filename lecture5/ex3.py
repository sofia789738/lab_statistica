#test function that calls the new methods and verificates their behaviour.

import fraction_lib

def main() :
    fraction1 = fraction_lib.Fraction(2, 3)
    fraction2 = fraction_lib.Fraction(3, 4)

    my_sum = fraction1 + fraction2
    print('sum:')
    my_sum.print() 

    my_diff = fraction1 - fraction2
    print ('\ndifference:')
    my_diff.print()

    my_div = fraction1 / fraction2
    print ('\ndivision:')
    my_div.print()
    

    my_prod = fraction1 * fraction2
    print ('\nproduct:')
    my_prod.print()

    





    



if __name__ == "__main__":
    main ()
