#Modificare la sezione_aurea_max_LLfunzione aggiungendo la stampa dei valori finali dell'intervallo a ogni iterazione, 
#per osservare il restringimento dell'intervallo durante l'esecuzione del programma.

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood

def golden_ratio_max_LL_modificated(xmin, xmax, likelihood, log_likelihood, randlist, pdf, prec=0.0001) :
    g = lambda tau : log_likelihood (likelihood, randlist, pdf, tau)
    r = (math.sqrt(5)-1)/2
    xi = xmin + (1-r)*(xmax-xmin)
    xf = xmin + r*(xmax-xmin)
    xi_list = [xi]
    xf_list = [xf]

    while (xmax-xmin) > prec :
        if g(xf) > g (xi) :
           xmin = xi
        else :
           xmax = xf 
        xf = xmin + r*(xmax-xmin)
        xi = xmin + (1-r)*(xmax-xmin)
        xi_list.append(xi)
        xf_list.append(xf)  

    return (xmax+xmin)/2. , xi_list, xf_list

def main () :
    #definire parametri
    tau_true = 2.
    N_events = 100
    xmin = 0.5
    xmax = 5.
    #calcolare e stampare tau_hat e gli intervalli usati da golden_ratio_LL
    sample = generate_exp (N_events, tau_true)
    tau_hat, x_iniziali, x_finali =  golden_ratio_max_LL_modificated (xmin, xmax, likelihood, log_likelihood, sample, exp_pdf, 0.0001)
    print ('il valore di tau che massimizza il logaritmo della verosimiglianza è:', tau_hat, '\n')
    print ('intervalli:\n')
    for i in range (0, len(x_finali)) :
        print ((x_iniziali)[i], (x_finali)[i], '\n')

if __name__ == "__main__" :
  main()