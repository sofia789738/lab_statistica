#Scrivi un programma che genera un set di 10 coppie (x,y) in modo che i punti siano distribuiti casualmente lungo l'asse orizzontale
#tra 0 e 10, e i punti sono costruiti utilizzando la formula y = f(x) + e (incertezza)

#Rappresentare graficamente il campione ottenuto, incluse le barre di errore previste.

import random
import matplotlib.pyplot as plt
from funzione import f
from math import sqrt

def rand_range (min, max) :
    x = min + (max-min)*random.random()
    return x

def rand_range_list (min, max, tot) :
    randlist = []
    for i in range (0,tot) :
         x = min + (max-min)*random.random()
         randlist.append (x)
    return randlist

def rand_TCL_ms (mean, sigma, N_sum = 10) :
    y = 0.
    delta = sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N_sum) :
        y = y + rand_range(xMin, xMax)
    y /= N_sum 
    return y 

def main () :
    #generazione delle coppie
    sigma_epsilon = random.random()
    randlist_x = rand_range_list (0, 10, 10)
    randlist_y = []
    epsilons = []
    for i in range (0,10) :
        epsilons.append(rand_TCL_ms(0., sigma_epsilon))
    for i in range (0,10) :
        randlist_y.append(f(randlist_x[i]) + epsilons[i])
    #rappresentazione dei dati
    sigma = [sigma_epsilon] * 10 #assumo la stessa incertezza per tutti i punti
    fig, ax = plt.subplots (1, 1)
    ax.set_title ('grafico a dispersione di un modello lineare')
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.errorbar(randlist_x, randlist_y, xerr = 0., yerr = sigma, linestyle = 'none', color = 'red') #linestyle=none per vedere solo barre di errore e non anche grafico che unisce i punti
    plt.show()

if __name__ == "__main__" :
    main()
