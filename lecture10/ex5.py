#Mostra graficamente che all'aumentare della dimensione del campione disponibile, 
#il profilo del logaritmo della funzione di verosimiglianza diventa più stretto.

#Per semplificare la visualizzazione, utilizzare il logaritmo del rapporto tra la funzione di verosimiglianza e il suo valore massimo

import matplotlib.pyplot as plt
import numpy as np
import math
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, golden_ratio_max_LL, loglikelihood_ratio
    

def main () :
   #definire parametri
    tau_true = 2.
    xmin = 0.1
    xmax = 5.
    N_events= [10, 100, 1000, 10000]
    colors = ['red', 'orange', 'yellow', 'green']
   
    #calcolare LogLikelihoodRatio al variare di N e rappresentare graficamente
    x_tau = np.linspace(xmin, xmax, 1000)
    fig, ax = plt.subplots (ncols=1, nrows=1)
    ax.set_xlabel ('tau')
    ax.set_ylabel ('Ratio log likelihood')
    ax.set_title ('confronto di Log-likelihood_ratio al variare di N numero di eventi')
    j = 0
    for N in N_events :
        sample = generate_exp (N, tau_true)
        tau_hat = golden_ratio_max_LL(xmin, xmax, likelihood, log_likelihood, sample, exp_pdf, prec = 0.001)
        y_loglik = []
        for i in range (0, x_tau.size) :
            y_loglik.append (loglikelihood_ratio(x_tau[i], exp_pdf, sample, tau_hat))
        plt.plot (x_tau, y_loglik, color = colors[j])
        j = 1 + j
        
    plt.show()


if __name__ == "__main__" :
   main()
