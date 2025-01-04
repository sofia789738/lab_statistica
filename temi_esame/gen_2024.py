import numpy as np
import matplotlib.pyplot as plt
from math import floor, ceil
from scipy.stats import norm, chi2
from numeri_casuali import rand_range, generate_TAC, TCL_random
from stats import mean, variance, skewness, my_kurtosis, std_dev
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL

def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))

def HOM_integral (func, xmin, xmax, ymin, ymax, n_tot) :
    n_hit = 0
    for i in range (0, n_tot) :
        x = rand_range (xmin, xmax)
        y = rand_range (ymin, ymax)
        if (func(x) > y) :
             n_hit = n_hit + 1
    A = float((xmax-xmin) * (ymax-ymin))
    p = float (n_hit / n_tot)
    int = p * A
    return int

def f (x) :
    return (np.cos(x)**2)

def main () :
    # data una pdf calcolare il valore di B affinchè la pdf f sia normalizzata utilizzando il metodo hir or miss
    xmin = 0
    xmax = 1.5*np.pi
    ymin = 0
    area_i = HOM_integral (f, xmin, xmax, ymin, 1, 10000)
    area_f = 1.
    B = area_f/area_i #fattore di normalizzazione tale per cui l'area sottesa dalla pdf è 1
    print('area prima della normalizzazione:', area_i)
    print('fattore di normalizzazione:', B)

    #genarare N = 10000 eventi generati con il metodo try and catch secondo la pdf f normalizzata
    N = 10000
    sample = generate_TAC (f, xmin, xmax, 1, N)

    #mostrare in un istogramma gli eventi generati
    xMin = min(sample)
    xMax = max(sample)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (sample, bins = bin_edges, color = 'blue') 
    ax.set_title ('numeri casuali distribuiti secondo f')
    ax.set_xlabel ('x')
    ax.set_ylabel ('conteggi')

    #calcolare a partire dagli eventi generati media, varianza, asimmetria e curtosi
    v = np.array (sample)
    print ('mean    :', mean (v))
    print ('sigma   :', variance (v))
    print ('skewness:', skewness (v))
    print ('kurtosis:', my_kurtosis (v))

    #mostrare quantitivamente che il teorema centrale del limite vale, 
    #a partire dalla generazione di numeri pseudo-casuali con la tecnica del TCL applicata a f
    gaus_sample = []
    for i in range (0, 10000) :
        gaus_sample.append(TCL_random(0., xmin, xmax, tot= 10))
    media_gaus = mean(np.array(gaus_sample))
    sigma_gaus = std_dev(np.array(gaus_sample))
    xMin = floor(min(gaus_sample)) 
    xMax = ceil(max(gaus_sample))
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(10000)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (gaus_sample, bins = bin_edges, color = 'red') 
    plt.show()
    #valuto accordo delle misure binnate con una gaussiana
    bin_content, bin_edges = np.histogram (gaus_sample, bins = n_bins, range = (xmin, xmax)) 
    def modello_bin (bin_edges, mu, sigma) :
         return N*norm.cdf (bin_edges, mu, sigma)
    f_costo_bin = ExtendedBinnedNLL(bin_content, bin_edges, modello_bin)
    my_minuit = Minuit(f_costo_bin, mu = media_gaus, sigma = sigma_gaus)
    my_minuit.migrad ()
    my_minuit.minos ()
    if 1. - chi2.cdf (my_minuit.fval, df = my_minuit.ndof) > 0.10:
        print ('the event sample is compatible with a Gaussian distribution')


if __name__ == "__main__":
    main ()
