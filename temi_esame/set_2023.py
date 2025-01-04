#implementare una libreria che generi numeri pseudo casuali distribuiti secondo una pdf di Cauchy
#la funzione deve prendere come argomenti M, alpha e la semilarghezza dell'intervallo di generazione

import random

def f_cauchy (x, M, alpha) :
     return (1/np.pi)*alpha/(((x-M)**2) + alpha**2)

def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x

def rand_TAC_cauchy (M, alpha, semilarghezza) :
    x = rand_range (M - semilarghezza, M + semilarghezza)
    ymax = f_cauchy (M, M, alpha) #la distribuzione di cauchy ha massimo nel centro
    y = rand_range (0, ymax)
    while (y > f_cauchy (x, M, alpha)) :
        x = rand_range (M - semilarghezza, M + semilarghezza)
        y = rand_range (0, ymax)
    return x

def rand_TCL_cauchy (M, alpha, semilarghezza, N = 100) :
     sum = 0.
     for i in range (0, N) :
          x = rand_TAC_cauchy (M, alpha, semilarghezza)
          sum = sum + x
     average = sum / N
     return average

#scrivere un programma che verifichi il funzionamento della libreria
#N numeri generati tra (M - 3alpha) e (M + 3alpha)
#N, M, alpha presi come parametri dalla linea di comando
import sys
import matplotlib.pyplot as plt
import numpy as np
from visualizzazione import sturges
from stats import mean, std_dev
from scipy.stats import norm, chi2
from iminuit import Minuit
from iminuit.cost import UnbinnedNLL
from IPython.display import display

def main () :
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    alpha = int(sys.argv[3])
    x = []
    for i in range (0, N) :
         x.append (rand_TAC_cauchy(M, alpha, 3*alpha))

#accumulare numeri casuali in un istogramma e disegnarlo
#scegliere min, max e numero di bin sulla base dei parametri inseriti
    xMin = min(x)
    xMax = max(x)
    n = len(x)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(n)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (x, bins = bin_edges, color = 'blue') 
    ax.set_title ('numeri casuali con distribuzione di Cauchy')
    ax.set_xlabel ('x')
    ax.set_ylabel ('conteggi')
    plt.savefig ('numeri_casuali_cauchy.png')

#calcolare media e sigma di numeri pseudo casuali distribuiti con pdf di cauchy
#distribuiti tra (M-i*alpha) e (m+i*alpha) al variare di i tra 1 e 100
    i_min = 1
    i_max = 100
    i_alpha = []
    media = []
    sigma = []
    while (i_min <= i_max) :
         i_alpha.append(i_min)
         x = []
         for i in range (0, N) :
             x.append (rand_TAC_cauchy(M, alpha, i_min*alpha))
         media.append(mean(np.array(x)))
         sigma.append(std_dev(np.array(x)))
         i_min = i_min + 1
#rappresentare separatamente l'andamento delle due quantità in funzione di i 
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (i_alpha, media, color= 'red')
    ax.set_title ('media della distribuzione in funzione della ampiezza', size=14)
    ax.set_xlabel ('i_alpha')
    ax.set_ylabel ('media')
    plt.savefig ('media_cauchy.png')
    plt.show()
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (i_alpha, sigma, color= 'red')
    ax.set_title ('sigma della distribuzione in funzione della ampiezza', size=14)
    ax.set_xlabel ('i_alpha')
    ax.set_ylabel ('sigma')
    plt.show ()
    plt.savefig ('sigma_cauchy.png')

    #implementare una funzione che generi numeri pseudo-casuali con la tecnica TCL a partire da numeri generati con pdf di Cauchy
    #verificare se i numeri così generati sono distribuiti con pdf gaussiana
    x_gaus = []
    N_gaus = 1000
    for i in range (0, N_gaus) :
         x_gaus.append (rand_TCL_cauchy(M, alpha, alpha))
    #determino fit dei dati     
    def modello_unb (x, mu, sigma) :
        return norm.pdf(x, mu, sigma)
    f_costo_unb = UnbinnedNLL (x_gaus, modello_unb)
    media = np.mean(x_gaus) 
    dev = np.std(x_gaus)
    my_minuit_unb = Minuit (f_costo_unb, mu = media, sigma = dev)
    my_minuit_unb.limits["sigma"] = (0, None)
    my_minuit_unb.migrad () 
    display (my_minuit_unb)
    #valuto bontà del fit
    Q_squared = my_minuit_unb.fval
    df = my_minuit_unb.ndof
    p_value = 1 - chi2.cdf (Q_squared, df)
    print ('Q quadro:', Q_squared)
    print ('gradi di libertà:', df)
    print ('p-value associato:', p_value)
    
    
    
if __name__ == "__main__":
    main ()