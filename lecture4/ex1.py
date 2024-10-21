#write a function that implements the linear generator pseudo-random numbers

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
    print(rand(10, 0))
    


if __name__ == "__main__" :
    main()