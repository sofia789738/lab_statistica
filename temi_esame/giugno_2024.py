from numeri_casuali import generate_exp, generate_TCL_ms
from visualizzazione import sturges
from stats import mean, std_dev
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import expon, norm
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL
from IPython.display import display

def main () :
    #generare un campione di N_exp = 2000 eventi distribuiti con pdf esponenziale nota lambda (tau = 1/lambda)
    #generare un campione di N_gau = 200 eventi distribuiti con pdf gaussiana noti mu e sigma
    N_exp = 2000
    N_gau = 200
    tau = 200 
    mu = 190
    sigma = 20
    x_exp = generate_exp (N_exp, tau)
    x_gau = generate_TCL_ms (mu, sigma, N_gau)

    #costruire un campione pari all'unione dei due precedenti e rappresentarlo in un istogramma
    x = x_exp + x_gau
    n = len(x)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(n)
    bin_content, bin_edges = np.histogram (x, bins=n_bins)
    ax.hist (x, bins = bin_edges, color = 'pink') 
    ax.set_xlabel ('x')
    ax.set_ylabel ('conteggi')
    plt.show()
    
    #eseguire un fit del campione per determinare i parametri del modello
    def modello (bin_edges, N_signal, mu, sigma, N_background, tau): #modello totale dell'istogramma
            return N_signal * norm.cdf (bin_edges, mu, sigma) + N_background * expon.cdf (bin_edges, tau) 
    f_costo = ExtendedBinnedNLL (bin_content, bin_edges, modello) #funzione di costo 
    media = mean (x)
    sigma = std_dev (x)
    my_minuit = Minuit (f_costo, N_signal = n, mu = media, sigma = sigma, N_background = n, tau = 1.) #minimizzazione con suggerimenti
    my_minuit.limits['N_signal', 'N_background', 'sigma', 'tau'] = (0, None) 
    my_minuit.migrad () #attuo minimizzazione
    display (my_minuit)

    #si costruisca una funzione che calcoli il logaritmo della verosimiglianza associata al campione
    #dato un modello f(x) = a * exp (-x*tau) + b * gauss (x, mean, sigma)
    #a e b fattori di normalizzazione
    #fisso tutti i parametri tranne uno
    tau_hat = my_minuit.values ['tau']
    sigma_hat = my_minuit.values ['sigma']
    n_exp = my_minuit.values ['N_background']
    n_gau = my_minuit.values ['N_signal']
    n_tot = n_exp + n_gau
    a = n_exp / n_tot
    b = n_gau / n_tot
    def f (theta, sample) :
        return a/tau_hat * np.exp (-sample/tau_hat) + b*norm.pdf (sample, theta, sigma_hat)
    def log_likelihood (theta, pdf, sample) :
       logL = 0.
       for x in sample:
          if (pdf (x, theta) > 0.) : 
              logL = logL + np.log (pdf (x, theta))    
       return logL
    
    #fissati i parametri del modello al risultato ottenuto dal fit, si calcoli il valore del logaritmo della verosimiglianza
    #per il campione dato il modello, variando il valore del parametro mean, fra 30 e 300, 
    #con passo costante e se ne disegni l'andamento
    medie = []
    l = []
    media_min = 30
    media_max = 300
    while media_min < media_max :
        medie.append (media_min)
        l.append (log_likelihood(media_min, f, x))
        media_min = media_min + 1
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (medie, l, color = 'blue')
    ax.set_title ('andamento del log-likelihood', size=14)
    ax.set_xlabel ('media')
    ax.set_ylabel ('log_likelihood')
    plt.show ()

    #si determini il massimo della funzione di verosimiglianza poc'anzi costruita in funzione del parametro mean, 
    #utilizzando l'algoritmo della sezione aurea
    def golden_ratio_max_LL(xmin, xmax, log_likelihood, randlist, pdf, prec=0.0001) :
      g = lambda mean : log_likelihood (mean, pdf, randlist)
      r = (math.sqrt(5)-1)/2
      xf = xmin + r*(xmax-xmin)
      xi = xmin + (1-r)*(xmax-xmin)
      while (xmax-xmin) > prec :
         if g(xf) > g (xi) :
             xmin = xi
         else :
            xmax = xf 
         xf = xmin + r*(xmax-xmin)
         xi = xmin + (1-r)*(xmax-xmin)
      mean_hat = (xmax+xmin)/2.   
      return mean_hat
    
    mean_hat = golden_ratio_max_LL (30, 300, log_likelihood, x, f)
    print ('stima della media dalla massimizzazione della verosimiglianza:', mean_hat)

    
if __name__ == "__main__" :
    main()