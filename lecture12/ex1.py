#Prestare attenzione a determinare l'intervallo e il binning dell'istogramma utilizzato per l'adattamento in base agli eventi stessi, 
#scrivendo algoritmi appropriati per determinare il minimo e il massimo del campione e una stima ragionevole del numero di bin da utilizzare.

#Determinare i valori iniziali dei parametri di adattamento utilizzando le tecniche descritte nella lezione.

#Stampa il risultato dell'adattamento sullo schermo.

#Quali parametri sono correlati e quali sono anti-correlati tra loro?

import numpy as np
import matplotlib.pyplot as plt
from math import floor, ceil
from scipy.stats import expon, norm
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL
from IPython.display import display

def main () :
    #ISTOGRAMMA
    with open ('dati.txt') as input_file:
      sample = [float (x) for x in input_file.readlines()]
      xmin = floor(min(sample)) #arrotondo dal basso
      xmax = ceil(max(sample))  #arrotondo dall'alto
      xrange = range (xmin, xmax)
      n_bins = len(sample) / 100 #stima del numero di bin
      bin_content, bin_edges = np.histogram (sample, bins = n_bins, range = xrange) #uso le caratteristiche dell'istogramma per una prima stima del contenuto e della larghezza dei bin

      fig, ax = plt.subplots (nrows=1, ncols=1)
      ax.hist (sample, color = 'blue', bins = bin_edges) 
      ax.set_title ('dati.txt')
      ax.set_xlabel('variable')
      ax.set_ylabel('events in bin')
      plt.show ()

      #DETERMINARE PARAMETRI DI ADATTAMENTO
      n_events = len(sample) 
      mean = np.mean(sample) #prima stima della media
      sigma = np.std(sample) #prima stima della deviazione standard

      def modello (bin_edges, N_signal, mu, sigma, N_background, tau):
            return N_signal * norm.cdf (bin_edges, mu, sigma) + N_background * expon.cdf (bin_edges, 0, tau)

      f_costo = ExtendedBinnedNLL (bin_content, bin_edges, modello) #funzione da minimizzare

      my_minuit = Minuit (f_costo, N_signal = n_events, mu = mean, sigma = sigma, N_background = n_events, tau = 1.) 
                  #parametri di input, cioè valori iniziali dei parametri di 'modello' per aiutare Minuit a trovare i paremetri che minimizzino 'f_costo'
                  #fornisco a Minuit suggerimenti non lontani dal risultato finale
                  #tau > 0 per avere esponenziale decrescente
      my_minuit.limits['N_signal', 'N_background', 'sigma', 'tau'] = (0, None) #impongo ad alcuni parametri di essere >0

      #determino una stima dei parametri di fondo fissando i parametri del segnale
      my_minuit.values ["N_signal"] = 0
      my_minuit.fixed ["N_signal", "mu", "sigma"] = True
      centro = 0.5 * (bin_edges[1:] + bin_edges[:-1]) #valore centrale sull'asse x
      f_costo.mask = (centro < 5) and (15 < centro)
                     #il segnale non di fondo corrisponde ad una gaussiana centrata in 10
                     #considero tutti quei dati che si trovano in corrispondenza delle code della gaussiana, cioè che sono dovuti dal segnale di fondo
                     #nuova funzione di costo che considera solo un tratto dell'array bin_edges, cioè i bin con x_centro < 5 o x_centro > 15
      my_minuit.migrad () #trova tau e N_background
      my_minuit.minos () #trova intervalli di confidenza di tau e N_background
      print (my_minuit.valid)
      display (my_minuit)

      #determino una stima dei parametri del segnale ignorando il segnale di fondo
      f_costo.mask = None #rimuovo la restrizione precedente
      my_minuit.fixed = False #libero i parametri precendentemente fissati
      my_minuit.fixed["N_background", "tau"] = True 
      my_minuit.values["N_signal"] = n_events - my_minuit.values["N_background"] 
                                   #fisso il numero di dati provenienti dal segnale perchè so quanti sono dovuti dal segnale di fondo
      my_minuit.migrad ()
      my_minuit.minos ()
      print (my_minuit.valid)
      display (my_minuit)

      #realizzo adattamento finale (considerando tutto il segnale)
      my_minuit.fixed = False # ri-libero i parametri precedentemente fissati
      my_minuit.migrad () 
      my_minuit.minos ()
      print (my_minuit.valid)
      display (my_minuit)

      #stampo risultati e relativi errori
      print (my_minuit.parameters)
      my_err = my_minuit.errors
      for elem in my_err:
         print (elem + ' : + ', str (my_minuit.merrors[elem].upper), ' ' + str (my_minuit.merrors[elem].lower))
      for i in my_minuit.parameters :
           print ('parameter ', i, ': ', str (my_minuit.values[i]), ' +- ', str (my_minuit.errors[i]), '   |   ', str (my_minuit.merrors[i].upper), ' ', str (my_minuit.merrors[i].lower))
      
      #per capire se i parametri sono collegati stampo matrice di covarianza
      print (my_minuit.covariance)
      print (my_minuit.covariance.correlation ())

      
if __name__ == "__main__":
    main ()