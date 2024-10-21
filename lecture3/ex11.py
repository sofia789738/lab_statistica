#write a program to draw overlaid poisson distribution functions using different means

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

def main() :
    m1 = 1
    m3 = 3
    m5 = 5
    x1 = np.linspace(-10, 20, 100)
    x3 = np.linspace(-10, 20, 100)
    x5 = np.linspace(-10, 20, 100) 
    y1 = poisson.pmf(x1, m1)
    y3 = poisson.pmf(x3, m3)
    y5 = poisson.pmf(x5, m5)
    plt.plot(x1, y1, label="poisson1", color='blue')
    plt.plot(x3, y3, label="poisson3", color='red')
    plt.plot(x5, y5, label="poisson5", color='green')
    plt.title('overlaid Poisson distribution functions')
    plt.savefig('poisson_pmf')

    




if __name__ == "__main__":
    main ()