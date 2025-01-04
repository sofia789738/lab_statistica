#Utilizzando la tecnica degli esperimenti giocattolo, tracciare il grafico della distribuzione di probabilità dello stimatore τ.
#Sovrapporre l'istogramma generato con il grafico dello stimatore e l'intervallo di confidenza trovati nell'esercizio precedente.
#Confrontare il valore di σ τ ottenuto nell'esercizio precedente con quello calcolato dalla distribuzione dei numeri salvati nell'elenco.

import numpy as np
import matplotlib.pyplot as plt
from math import floor
from lib import std_dev
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, loglikelihood_ratio, golden_ratio_max_LL
from ex6 import intersect_LLR

def main () :
   #settare parametri
   tau_true = 2.
   N_evt    = 50
   N_toys   = 1000

   #calcolare tau_hat e la precisione sul suo valore (come per esercizio 6)
   sample = generate_exp (N_evt, tau_true)
   tau_hat = golden_ratio_max_LL (0.5, 5., likelihood, log_likelihood, sample, exp_pdf, 0.0001)    
   tau_hat_minusS = intersect_LLR (loglikelihood_ratio, exp_pdf, sample, 0.5, tau_hat, -0.5, tau_hat)
   tau_hat_plusS = intersect_LLR (loglikelihood_ratio, exp_pdf, sample, tau_hat, 5., -0.5, tau_hat)
   
   #calcolare più volte tau_hat usando N_toys esperimenti giocattolo
   tau_hats = []
   for i in range (N_toys) :
       singleToy = generate_exp (N_evt, tau_true)
       tau_hat_toy = golden_ratio_max_LL (0.5, 5., likelihood, log_likelihood, singleToy, exp_pdf, 0.0001)
       tau_hats.append (tau_hat_toy)
   
   xMin = 1.
   xMax = 3.
   bin_edges = np.linspace (xMin, xMax, floor (N_toys/20)) 
   fig, ax = plt.subplots ()
   ax.set_title ('Tau_hat expected distribution', size=14)
   ax.set_xlabel('tau_hat')
   ax.set_ylabel('events in bin')
   ax.hist (tau_hats, bins = bin_edges, color = 'orange',)
   limits = ax.get_ylim ()
   plt.plot ([tau_hat, tau_hat], limits, color = 'blue')
   plt.plot ([tau_hat_minusS, tau_hat_minusS], limits, color = 'blue', linestyle = 'dashed')
   plt.plot ([tau_hat_plusS, tau_hat_plusS], limits, color = 'blue', linestyle = 'dashed')

   #confrontare sigma di tau ottemuta con i due diversi metodi 
   sigma = std_dev(np.array(tau_hats))
   print ('sigma ricavata dai toy:      ', sigma)
   print ('sigma con il metodo grafico: ', 0.5 * (tau_hat_plusS - tau_hat_minusS))
   plt.show ()

if __name__ == "__main__" :
   main()