import random
import math
import numpy as np
import matplotlib.pyplot as plt
from stats import mean, variance, unc_mean, unc_variance

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

#Si scriva una funzione che generi coppie di numeri pseudo-casuali distribuiti secondo una densit`a di probabilit`a Gaussiana
# utilizzando l'algoritmo di Box-M"uller implementata in una libreria dedicata.

def generate_gaus_bm (N) :
    g1_v = []
    g2_v = []
    for i in range (0,N) :
        x1 = random.random()
        x2 = random.random()
        g1 = math.sqrt (-2*np.log(x1)) * np.cos(2*np.pi*x2)
        g2 = math.sqrt (-2*np.log(x1)) * np.sin(2*np.pi*x2)
        g1_v.append(g1)
        g2_v.append(g2)
    return g1_v, g2_v

def generate_gaus_bm_mod (N, mu, sigma) :
    g1_mod = []
    g2_mod = []
    for i in range (0,N) :
         x1 = random.random()
         x2 = random.random()
         g1 = math.sqrt (-2*np.log(x1)) * np.cos(2*np.pi*x2)
         g2 = math.sqrt (-2*np.log(x1)) * np.sin(2*np.pi*x2)
         g1_new = g1*sigma + mu
         g2_new = g2*sigma + mu
         g1_mod.append(g1_new)
         g2_mod.append(g2_new)

    return g1_mod, g2_mod


#Si generino N = 1000 numeri pseudo-casuali utilizzando la funzione appena sviluppata e li si disegni in un istogramma, 
#scegliendone con un algoritmo opportuno gli estremi ed il binnaggio.
def main () :
    N = 1000
    x1, x2 = generate_gaus_bm (int(N/2))
    x = x1 + x2
    xmin = min(x)
    xmax = max(x)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N)
    bin_edges = np.linspace (xmin, xmax, n_bins)
    ax.hist (x, bins = bin_edges, color = 'blue') 
    ax.set_title ('algoritmo di Box Muller')
    ax.set_xlabel ('x')
    ax.set_ylabel ('conteggi')

#determinare media e varianza della distribuzione ottenuta e relativi errori
    v = np.array(x)
    media = mean(v)
    varianza = variance(v)
    inc_media = unc_mean (v)
    inc_varianza = unc_variance (v)
    print ('media:', media, '±', inc_media) 
    print ('varianza:', varianza, '±', inc_varianza) 

#Si mostri graficamente che, al variare del numero N di eventi generati, la sigma della distribuzione non cambia, 
#mentre l'errore sulla media si riduce
    N_max = 100000
    N_min = 10
    varianze = []
    inc_medie = []
    N = []
    while (N_min < N_max) :
        x1, x2 = generate_gaus_bm (int(N_min/2))
        x = x1 + x2
        v = np.array(x)
        varianze.append(variance(v))
        inc_medie.append(unc_mean(v))
        N.append(N_min)
        N_min = N_min * 10
    #rappresentazione
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (N, varianze, label='varianza', color = 'red')
    ax.plot (N, inc_medie, label='errore sulla media', color = 'green')
    ax.set_title ('incertezze al variare di N', size=14)
    ax.set_xlabel ('N')
    ax.legend () 
    ax.set_xscale ('log')
    ax.set_yscale ('log')
        
#Si trasformi l'algoritmo in modo che generi numeri pseudo-casuali con densit`a di probabilit`a Gaussiana con media 5 e varianza 4
#Si generi un nuovo campione di 1000 eventi con il nuovo algoritmo e se ne disegni la distribuzione, 
#sempre scegliendo in modo opportuno gli estremi ed il binnaggio dell'istogramma corrispondente.
    N = 1000
    media = 5
    varianza = 4
    x1_mod, x2_mod = generate_gaus_bm_mod (N, media, math.sqrt(varianza))
    x_mod = x1_mod + x2_mod
    xmin = min(x_mod)
    xmax = max(x_mod)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N)
    bin_edges = np.linspace (xmin, xmax, n_bins)
    ax.hist (x_mod, bins = bin_edges, color = 'pink') 
    ax.set_title ('algoritmo di Box Muller con media e varianza fissate')
    ax.set_xlabel ('x')
    ax.set_ylabel ('conteggi')
    plt.show ()
        
        
if __name__ == "__main__":
    main ()