from math import sqrt
from numeri_casuali import rand_range
from stats import mean, variance, skewness, my_kurtosis
from visualizzazione import sturges
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats 
from iminuit import Minuit
from iminuit.cost import BinnedNLL, ExtendedBinnedNLL
from IPython.display import display

#scrivere funzione che simuli un cammino con direzione casuale uniforme angolarmente
#e lunghezza distribuita gaussianamente con mean=1 e sigma = 0.2 troncata a valori positivi
def rand_TCL_positivi (mean, sigma, N_sum = 10) :
    y = 0.
    delta = sqrt (3 * N_sum) * sigma
    xMin = 0
    xMax = mean + delta
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum 
    return y 

def cammini (mean, sigma) :
    lunghezza = rand_TCL_positivi (mean, sigma)
    direzione = rand_range (0, 2*np.pi) #angolo in radianti
    return lunghezza, direzione

#immaginando l'origine del cammino in (0,0) scrivere funzione che calcoli posizione (x,y) dopo N=10 passi 
#disegnare il suo percorso
def posizione (passi, mean, sigma) :
    xstep = 0.
    ystep = 0.
    x = []
    y = []
    for i in range (0, passi) :
        l, alpha = cammini (mean, sigma)
        xstep = xstep + l * np.cos(alpha)
        ystep = ystep + l * np.sin(alpha)
        x.append (xstep)
        y.append (ystep)
    xf = xstep
    yf = ystep
    return x, y, xf, yf

def posizione_1 (passi, mean, sigma) :
    xstep = 0.
    ystep = 0.
    x = []
    y = []
    for i in range (0, passi) :
        l, alpha = cammini (mean, sigma)
        xstep = xstep + np.cos(alpha)
        ystep = ystep + np.sin(alpha)
        x.append (xstep)
        y.append (ystep)
    xf = xstep
    yf = ystep
    return x, y, xf, yf

def main () :
    media = 1.
    sigma = 0.2
    passi = 10
    x_coord, y_coord, x_finale, y_finale = posizione (passi, media, sigma)
    print ('posizione finale:', x_finale, y_finale)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (x_coord, y_coord, color = 'gold')
    ax.set_title ('percorso di Asterix', size=14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')

#considerare N=10000 cammini diversi, calcolare la posizione finale raggiunta per ogni cammino
#disegnare la distribuzione della distanza dal punto di partenza
    N_tot = 10000
    x = []
    y = []
    distanze = []
    for i in range (0, N_tot) :
        x_coord, y_coord, x_finale, y_finale = posizione (passi, media, sigma)
        x.append (x_finale)
        y.append (y_finale)
        d = sqrt (x_finale**2 + y_finale**2)
        distanze.append (d)
    
    xMin = min(distanze)
    xMax = max(distanze)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N_tot)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (distanze, bins = bin_edges, color = 'blue') 
    ax.set_title ('distribuzione delle distanze percorse')
    ax.set_xlabel ('d')
    ax.set_ylabel ('conteggi')
    plt.show ()
    
#determinare media, varianza, asimmetria e curtosi della distribuzione ottenuta
    d_array = np.array (distanze)
    print ('media:', mean(d_array))
    print ('varianza:', variance(d_array))
    print ('asimmetria:', skewness (d_array))
    print ('curtosi:', my_kurtosis(d_array))

#Se la lunghezza dei passi `e costante uguale ad 1, la distribuzione delle distanze r dopo N passi segue una distribuzione di Rayleigh
#si utilizzi un fit per determinare il numero di passi effettuato
    distanze_1 = []
    for i in range (0, N_tot) :
        x_coord, y_coord, x_finale, y_finale = posizione_1 (passi, media, sigma)
        d_1 = sqrt (x_finale**2 + y_finale**2)
        distanze_1.append (d_1)
    dmax = max (distanze_1)
    n_bins = sturges (N_tot)
    #adattamento del fit con algoritmo dei minimi quadrati per misure binnate
    #n = numero di passi
    bin_content, bin_edges = np.histogram (distanze_1, n_bins)
    def modello_bin (bin_edges, n):
        return N_tot * scipy.stats.rayleigh.cdf (bin_edges, loc = 0., scale = sqrt (n/2))
    f_costo_bin = ExtendedBinnedNLL (bin_content, bin_edges, modello_bin)
    m = Minuit (f_costo_bin, n = dmax)
    m.migrad ()
    m.minos ()
    print (m.valid)
    display (m)
    n_hat = m.values ['n']
    print ('numero di passi stimato dal fit:', n_hat)
    #chi quadro per valutare la bontà del fit
    Q_squared = m.fval
    df = m.ndof
    p_value = 1 - scipy.stats.chi2.cdf (Q_squared, df)
    print ('Q quadro:', Q_squared)
    print ('gradi di libertà:', df)
    print ('p-value associato:', p_value)
    

if __name__ == "__main__":
    main ()