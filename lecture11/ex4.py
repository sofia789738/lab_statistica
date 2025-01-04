#Utilizzando la tecnica degli esperimenti giocattolo, generare 10.000 esperimenti di adattamento con il modello studiato negli esercizi precedenti
#e riempire un istogramma con i valori ottenuti di Q^2

import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor
from iminuit import Minuit
from iminuit.cost import LeastSquares
from ex1 import rand_TCL_ms
from funzione import f, f_parametrizzata

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def mean (my_array) :
    n = np.size(my_array)
    tot = 0
    for i in range(0,n) :
        tot = tot + my_array[i]
    m = tot/n
    return m
    
def main () :
    #necessario per generare campioni simulati
    randlist_x = np.arange(0, 10, 1)
    randlist_y = np.zeros(10)
    epsilons = []

    #calcolo yi e ricavo i valori di Q^2 per N_tot esperimenti di adattamento
    N_tot = 10000
    Q_squared = []
    for j in range (0, N_tot) :
        sigma_epsilon = random.random()
        for i in range (0,10) :
            epsilons.append(rand_TCL_ms(0., sigma_epsilon))
        for i in range (0,10) :
            randlist_y[i] = f(randlist_x[i]) + epsilons[i]
        sigma_y = [sigma_epsilon] * 10

        minimi_quadrati = LeastSquares (randlist_x, randlist_y, sigma_y, f_parametrizzata) #genero Q^2 (funzione di costo)
        m_toy = Minuit (minimi_quadrati, m = 0., q = 0.) 
        m_toy.migrad ()
        m_toy.hesse () 
        Q_squared.append(m_toy.fval)

    #istogramma
    fig, ax = plt.subplots (1, 1)
    ax.set_title ('Q-squared distribution')
    n_bins = sturges(N_tot)
    QMin = min(Q_squared)
    QMax = max(Q_squared)
    bin_edges = np.linspace (0, 4 * 8, floor (N_tot/100))
    ax.hist (Q_squared, bins = bin_edges, color = 'blue')

    plt.show()
  
if __name__ == "__main__" :
    main()

