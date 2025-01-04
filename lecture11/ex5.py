#Modificare il programma precedente cambiando deliberatamente l'incertezza sperimentale associata ai punti yi
#verificare che sia possibile recuperare l'incertezza utilizzata nella generazione dei punti attraverso il valore atteso della variabile Q^2

import random
import numpy as np
from math import sqrt
from iminuit import Minuit
from iminuit.cost import LeastSquares
from ex1 import rand_TCL_ms
from funzione import f, f_parametrizzata

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
    sigma_epsilon = random.random()
    for j in range (0, N_tot) :
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

    #calcolo e stampo il valore atteso di Q squared e l'incertezza associata agli yi (valutazione a posteriori)
    Q_squared_mean = mean(np.array(Q_squared))
    N_dof = N_tot - 2
    print ('average Q_squared expected value:', Q_squared_mean)
    print ('escalate factor', sqrt (Q_squared_mean/N_dof)) #il valore atteso di Q^2 min è n-k (gdl)
           #se il fattore di scala è diverso da 1 si ha un fattore alfa legato ad una errata stima di tutte le incertezze
    print ('sigma:', sigma_epsilon / sqrt (Q_squared_mean/N_dof)) #per trovare la vera incertezza divido quella modificata per il fattore di scala

if __name__ == "__main__" :
    main()
