#Modificare la loglikelihood funzione per calcolare il logaritmo del prodotto dei valori
#della funzione di densità di probabilità, anziché la somma dei singoli logaritmi

from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, golden_ratio_max_LL
import random
import matplotlib.pyplot as plt
import numpy as np
import math

def log_likelihood_modificated (likelihood, randlist, pdf, t0) :
    l = 0.
    L = 1.
    sample = np.array (randlist)
    for x in sample :
        L = L * pdf (x, t0)
    if L <= 0 : 
        return 0
    else :
       for x in sample :
          l = np.log (L)
       return l 
    
def main () :
    #definire parametri
    tau_true = 2.
    N_events = 100
    xmin = 0.5
    xmax = 5.
    #calcolare e stampare tau_hat usando due espressioni diverse della funzione loglikelihood
    sample = generate_exp (N_events, tau_true)
    tau_hat_1 =  golden_ratio_max_LL (xmin, xmax, likelihood, log_likelihood, sample, exp_pdf, 0.0001)
    print ('valore di tau che massimizza il logaritmo della verosimiglianza calcolato con la somma dei logaritmi:', tau_hat_1, '\n')
    tau_hat_2 =  golden_ratio_max_LL (xmin, xmax, likelihood, log_likelihood_modificated, sample, exp_pdf, 0.0001)
    print ('valore di tau che massimizza il logaritmo della verosimiglianza calcolato con il logaritmo del prodotto:', tau_hat_2)

if __name__ == "__main__" :
  main()