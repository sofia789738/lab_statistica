#Genera un file dati_2.txtcontenente 10.000 eventi distribuiti secondo una distribuzione di probabilità gaussiana.

#Scrivere un programma che adatti gli eventi salvati nel file dati_2.txt utilizzando i metodi di massima verosimiglianza binned e unbinned 

#Confrontare i risultati delle due tecniche.

import random
import numpy as np
import matplotlib.pyplot as plt
from math import floor, ceil
from scipy.stats import expon, norm
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL, UnbinnedNLL
from IPython.display import display
from math import sqrt


def rand_range (min, max) :
    x = min + (max-min)*random.random()
    return x

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
     #genero eventi distribuiti con pdf gaussiana
     N = 10000
     sample = []
     for i in range (0, N) :
         sample.append(rand_TCL_ms(5., 1.))
        
     #ADATTAMENTO NON BINNATO
     def modello_unb (x, mu, sigma) :
        return norm.pdf(x, mu, sigma)
     f_costo_unb = UnbinnedNLL (sample, modello_unb)
     mean = np.mean(sample) #stimo parametri per suggeririre a Minuit circa dove cercare mu e sigma
     dev = np.std(sample)
     my_minuit_unb = Minuit (f_costo_unb, mu = mean, sigma = dev)
     my_minuit_unb.limits["sigma"] = (0, None) #deviazione standard necessariamente positiva
     my_minuit_unb.migrad () #trovo parametri

     display (my_minuit_unb) #mostro risultati 
     mean_unb = [my_minuit_unb.values[0], my_minuit_unb.errors[0]]
     sigma_unb = [my_minuit_unb.values[1], my_minuit_unb.errors[1]]

     #ADATTAMENTO BINNATO
     xmin = floor(min(sample)) #arrotondo dal basso
     xmax = ceil(max(sample))  #arrotondo dall'alto
     n_bins = int(len(sample) / 100)
     bin_content, bin_edges = np.histogram (sample, bins = n_bins, range = (xmin, xmax)) 
                              #uso le caratteristiche dell'istogramma per una prima stima del contenuto e della larghezza dei bin
     
     def modello_bin (bin_edges, N_tot, mu, sigma) : #attenzione all'ordine: prima la variabile poi i parametri 
         return N_tot * norm.cdf (bin_edges, mu, sigma)
     f_costo_bin = ExtendedBinnedNLL(bin_content, bin_edges, modello_bin)
     my_minuit_bin = Minuit(f_costo_bin, N_tot = N, mu = mean, sigma = dev)
     my_minuit_bin.limits["N_tot", "sigma"] = (0, None)
     my_minuit_bin.migrad ()
     display (my_minuit_bin)
     mean_bin = [my_minuit_bin.values[1], my_minuit_bin.errors[1]] #il primo parametro trovato dall'adattamento è N_tot
     sigma_bin = [my_minuit_bin.values[2], my_minuit_bin.errors[2]]

     #CONFRONTO
     fig, axes = plt.subplots (nrows=2, ncols=1)
     #means
     axes[0].set_title ('compare means')
     axes[0].errorbar (mean_bin[0], 'binned', xerr = mean_bin[1], marker = 'o')   #marker per avere un punto in corrispondenza della media
     axes[0].errorbar (mean_unb[0], 'unbinned', xerr = mean_unb[1], marker = 'o') #marker per avere un punto in corrispondenza della media
     #sigmas
     axes[1].set_title ('compare sigmas')
     axes[1].errorbar (sigma_bin[0], 'binned', xerr = sigma_bin[1], marker = 'o')   #marker per avere un punto in corrispondenza della sigma
     axes[1].errorbar (sigma_unb[0], 'unbinned', xerr = sigma_unb[1], marker = 'o') #marker per avere un punto in corrispondenza della sigma
     
     plt.show()

if __name__ == "__main__":
    main ()