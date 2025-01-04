#Rappresenta graficamente il profilo della funzione di verosimiglianza e il punto identificato come suo massimo.

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, golden_ratio_max_LL

def main () :
    #definire parametri
    tau_true = 2.
    N_events = 100
    xmin = 0.5
    xmax = 5.

    #calcolare e stampare tau_hat (migliore stima di tau)
    sample = generate_exp (N_events, tau_true)
    tau_hat =  golden_ratio_max_LL (xmin, xmax, likelihood, log_likelihood, sample, exp_pdf, 0.0001)
    print ('il valore di tau che massimizza il logaritmo della verosimiglianza è:', tau_hat)

    #rappresentare graficamente loglikelihood in funzione di tau
    x_tau = np.linspace(xmin, xmax, 1000)
    y_loglik = []
    for i in range (0, x_tau.size) :
        y_loglik.append (log_likelihood(likelihood, sample, exp_pdf, x_tau[i]))
    fig, ax = plt.subplots (ncols=1, nrows=1)
    plt.plot (x_tau, y_loglik, color='green')
    ax.set_xlabel ('tau')
    ax.set_ylabel ('log likelihood')
    plt.axvline (x = tau_hat, color='red', label='tau hat')
    plt.show()

if __name__ == "__main__" :
    main()

