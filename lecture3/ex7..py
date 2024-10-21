#draw gaussian distribution and its cumulative function

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def main() :
    norm_fix = norm(10., 5.)
    x = np.linspace (-50.0, 50.0, 100)
    plt.plot (x, norm_fix.pdf(x), label="PDF")
    plt.show
    plt.savefig ('ex7_pdf')

    plt.clf()

    plt.plot (x, norm_fix.cdf(x), label="CDF")
    plt.show
    plt.savefig ('ex7_cdf')



if __name__ == "__main__":
    main ()
