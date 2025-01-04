#Utilizzare il metodo degli esperimenti con i giocattoli per riempire l'istogramma delle differenze (τ - τ vero ) 
#dato un numero di eventi per esperimento con i giocattoli.

#Calcolare la media e la sigma della distribuzione delle differenze e rappresentare graficamente i loro valori
#in funzione del numero di eventi disponibili per la stima, mostrando l'andamento su un grafico con il numero di eventi disponibili
#sull'asse orizzontale e il valore del parametro sull'asse verticale.

import numpy as np
import matplotlib.pyplot as plt
from lib import std_dev, mean
from maximum_likelihood_lib import generate_exp, exp_pdf, likelihood, log_likelihood, loglikelihood_ratio, golden_ratio_max_LL
from ex6 import intersect_LLR

def main () :
    #settare parametri
    tau_true = 2.
    N_evt_max = 50
    N_toys   = 1000
    sample_size = 5

    #calcolare gli scarti (τ - τ vero ), la loro media e la loro deviazione standard al variare del numero di eventi considerato
    N_events   = []
    deviations = []
    sigmas     = []
    while sample_size <= N_evt_max :
        scarti = []
        #per ogni esperimento giocattolo rilevare la distanza di tau_hat dal valore di tau_true
        for iToy in range (N_toys) :
            singleToy = generate_exp (sample_size, tau_true)
            tau_hat_toy = golden_ratio_max_LL (0.5, 5., likelihood, log_likelihood, singleToy, exp_pdf, 0.0001)
            scarti.append (tau_hat_toy - tau_true)
        #per ogni N eventi rilevare media e deviazione standard degli scarti
        deviations.append (mean(np.array(scarti)))
        sigmas.append (std_dev(np.array(scarti)))
        N_events.append (sample_size)
        sample_size = sample_size * 2

    #rappresentazione grafica
    fig, ax = plt.subplots ()
    ax.set_title ('average deviations', size=14)
    ax.set_xlabel ('number of events')
    ax.set_ylabel ('average deviation')
    ax.errorbar (N_events, deviations, xerr = 0.0, yerr = sigmas) 
    plt.show ()

if __name__ == "__main__" :
   main()

