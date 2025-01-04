#libreria di funzioni per determinare il parametro τ di una distribuzione esponenziale da un elenco di numeri
#riempito con numeri pseudo-casuali distribuiti secondo una distribuzione di densità di probabilità esponenziale.

import random
import numpy as np
import math

#1: generare eventi distribuiti esponenzialmente (con tau_t=vero valore di tau)
def generate_exp (n_tot, tau_t) :
    exp_randlist = []
    for i in range (0, n_tot) : 
        y = random.random()
        x = -tau_t * np.log(1-y)
        exp_randlist.append(x)
    return exp_randlist

#2: definire pdf del sample di eventi
def exp_pdf (x, tau_t) :
    if tau_t == 0. : 
        return 1.
    return (np.exp (-1 * x / tau_t)) / tau_t

#3: calcolare likelihood
def likelihood (randlist, pdf, t0) :
    L = 1.
    sample = np.array (randlist)
    for x in sample :
        L = L * pdf (x, t0)
    return L

#4: calcolare log-likelihood o log-likelihood_ratio
def log_likelihood (lik, randlist, pdf, t0) :
    l = 0.
    sample = np.array (randlist)
    L = lik (randlist, pdf, t0)
    if L <= 0 : 
        return 0
    else :
       for x in sample :
          l = l + np.log (pdf (x, t0))
       return l 

def loglikelihood_ratio (theta, pdf, sample, theta_hat) :
    l = 0.
    sample = np.array (sample)
    for x in sample :
         l = l + np.log (pdf (x, theta)) - np.log(pdf(x, theta_hat))
    return l 
    
#5: trovare il massimo della verosimiglianza: uso algoritmo della sezione aurea assumendo tau compreso tra xmax e xmin
def golden_ratio_max_LL(xmin, xmax, likelihood, log_likelihood, randlist, pdf, prec=0.0001) :
    g = lambda tau : log_likelihood (likelihood, randlist, pdf, tau)
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    while (xmax-xmin) > prec :
        if g(xf) > g (xi) :
           xmin = xi
        else :
           xmax = xf 
        xf = xmin + r*(xmax-xmin)
        xi = xmin + (1-r)*(xmax-xmin)
    tau_hat = (xmax+xmin)/2.   
    return tau_hat

#6: confrontare il risultato ottenuto con la media dei numeri salvati nell'elenco
def exp_mean (exp_randlist) :
    exp_randarray = np.array(exp_randlist)
    n = np.size(exp_randarray)
    tot = 0
    for i in range (0, n) :
        tot = tot + exp_randarray [i]
    tau = tot / n
    return tau
    




