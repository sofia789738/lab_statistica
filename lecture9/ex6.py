#Study the behavior of the shape of the log-likelihood 
#as a function of the number of events comprising the generated sample.

from ex5 import likelihood, log_likelihood, exp_pdf
import random
import matplotlib.pyplot as plt
import numpy as np

def generate_exp (n_tot, t0) :
    exp_randlist = []
    for i in range (0, n_tot) : 
        y = random.random()
        x = -t0 * np.log(1-y)
        exp_randlist.append(x)
    return exp_randlist

def main () :
    t0 = 5. #fixed tau
    N_events = np.linspace (0, 1000, 100)
    randlist = generate_exp (int(max(N_events)), t0)
    log_lik = []
    for i in range (0, N_events.size) :
        randlist_i = randlist[:i] #to consider elemnts of the generated sample till the index i
        log_lik.append(log_likelihood(likelihood, randlist_i, exp_pdf, t0))
    
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.set_title ('log-likelihood as a function of the number of events')
    ax.set_xlabel ('N events')
    ax.set_ylabel ('log likelihood')
    plt.plot (N_events, log_lik, color = 'purple')
    plt.show()


if __name__ == "__main__":
    main ()

