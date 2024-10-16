#calculate parameters of an array
import numpy as np
from lib import mean, variance, std_dev

def main() :
     a = np.array ([1, 7, 9, 5, 6, 90, 13, 5, 55, 568, 98, 97, 512, 87])
     print(mean(a),'\n')
     print(variance(a),'\n')
     print(std_dev(a), '\n')
          
if __name__ == "__main__" :
    main()
