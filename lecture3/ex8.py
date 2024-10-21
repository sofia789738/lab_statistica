import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def main() :
   x = np.linspace (0., 100.0, 100)
   pdf = st.expon.pdf(x, loc=0, scale=4)
   plt.plot(x, pdf, label="expPDF")
   plt.savefig('ex8_exp')





         
if __name__ == "__main__":
    main ()