#Utilizzare il metodo di bisezione per trovare i due punti τ - σ τ e τ + σ τ 

#Rappresentare graficamente il profilo di verosimiglianza, i valori dello stimatore 
#e l'intervallo di confidenza insieme al segmento orizzontale utilizzato per la sua determinazione.

import matplotlib.pyplot as plt
import numpy as np
import math
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, golden_ratio_max_LL

def loglikelihood_ratio (theta, pdf, sample, theta_hat) :
    l = 0.
    sample = np.array (sample)
    for x in sample :
         l = l + np.log (pdf (x, theta)) - np.log(pdf(x, theta_hat))
    return l 

def intersect_LLR (
    g,              # funzione di cui trovare lo zero
    pdf,            # pdf degli eventi considerati
    sample,         # sample degli eventi
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo 
    ylevel,         # valore dell'intersezione orizzontale
    theta_hat,      # max della likelihood    
    prec = 0.0001): # precisione della funzione        

    def gprime (x) :
        return g (x, pdf, sample, theta_hat) - ylevel

    xAve = xMin 
    while ((xMax - xMin) > prec) :
        xAve = 0.5 * (xMax + xMin) 
        if (gprime (xAve) * gprime (xMin) > 0.) : xMin = xAve 
        else                                    : xMax = xAve 
    return xAve 


def main () :
    #definire parametri
    tau_true = 2.
    N_events = 100

    #calcolare tau_hat e la precisione sul suo valore
    sample = generate_exp (N_events, tau_true)
    tau_hat = golden_ratio_max_LL (0.5, 5., likelihood, log_likelihood, sample, exp_pdf, 0.0001)    
    tau_hat_minusS = intersect_LLR (loglikelihood_ratio, exp_pdf, sample, 0.5, tau_hat, -0.5, tau_hat)
    tau_hat_plusS = intersect_LLR (loglikelihood_ratio, exp_pdf, sample, tau_hat, 5., -0.5, tau_hat)

    #rappresentazione grafica
    fig, ax = plt.subplots ()
    ax.set_title ('Log-likelihood scan', size=14)
    ax.set_xlabel ('tau')
    ax.set_ylabel ('log likelihood')
    xMin = tau_hat_minusS - (tau_hat - tau_hat_minusS)
    xMax = tau_hat_plusS + (tau_hat_plusS - tau_hat)
    tauaxis = np.linspace (xMin, xMax, 10000)
    llr     = np.arange (0., tauaxis.size)
    for i in range (tauaxis.size) :
        llr[i] = loglikelihood_ratio(tauaxis[i], exp_pdf, sample, tau_hat)
    plt.plot (tauaxis, llr, 'r')
    limits = ax.get_ylim ()
    plt.plot ([tau_hat, tau_hat], limits, color = 'blue')
    plt.plot ([tau_hat_minusS, tau_hat_minusS], limits, color = 'blue', linestyle = 'dashed')
    plt.plot ([tau_hat_plusS, tau_hat_plusS], limits, color = 'blue', linestyle = 'dashed')
    plt.plot (plt.xlim (), [-0.5, -0.5], color = 'gray')

    plt.show ()

if __name__ == "__main__" :
   main()