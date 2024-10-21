import numpy as np
import matplotlib.pyplot as plt

#Write a program that draws the basic trigonometric functions over a meaningful domain, using NumPy universal functions

def main() :
    x = np.linspace(-10, 10, 100)
    cos = np.cos(x)
    sin = np.sin(x)
    plt.plot(x, cos, label="cosx", color='green')
    plt.plot(x, sin, label="sinx", color='yellow')
    plt.title('trigonometrical functions')
    plt.savefig('trig_ex8')

    
    
if __name__ == "__main__" :
    main()
