#Show that initializing the seed of the linear congruential pseudo-random integer generator is equivalent
#to looking into a sequence of pseudo-random numbers at any point.

import sys

def rand(tot, seed) :
    sequence = []
    x = seed
    M = 2147483647
    A = 214013
    C = 2531011
    for i in range (0, tot) :
        x = (A*x + C) % M
        sequence.append(x)
    return sequence

def main () :
    mysequence = rand (10, int(sys.argv[1]))
    print(mysequence)
    point = int(input('insert point of the sequence\n'))
    print ("ind: ", mysequence[point])
    print(rand (10, mysequence[point]))


if __name__ == "__main__" :
    main()