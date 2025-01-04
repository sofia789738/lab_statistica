import numpy as np
import matplotlib.pyplot as plt
import sys
from math import sqrt
from numeri_casuali import generate_TCL_ms, rand_TCL_ms
from iminuit import Minuit
from iminuit.cost import LeastSquares
from scipy.stats import chi2
from IPython.display import display
from stats import mean

#generare 6 coppie di numeri pesudo casuali lungo l'andamento di f(x)
#xi fissati e yi disstribuiti attorno f(xi) con pdf gaussiana con sigma inserita da riga di comando
#usare algoritmo TCL per generare errori ei (sigma yi), note media e sigma della gaussiana

def f (x) :
    return 2*np.sin (0.5*x+ 0.78) + 0.8

def f_par (x, p0, p1, p2, p3) :
    return p0*np.sin (p1*x + p2) + p3

def trova_max (y, N) :
    j = 0
    i = 0
    y_max = y[0]
    while i < N-1:
        if y[i] > y [i+1] :
            j = j
        else :
            j = j+1
        i = i + 1
    return j

def trova_min (y, N) :
    j = 0
    i = -1
    y_max = y[0]
    while i < N-1:
        if y[i] < y [i+1] :
            j = j
        else :
            j = j+1
        i = i + 1
    return j

def main () :
   N = 6
   x = [0.5, 2.5, 4.5, 6.5, 8.5, 10.5]
   e_sigma = float(sys.argv[1])
   e_mean = 0.
   e = generate_TCL_ms (e_mean, e_sigma, N)
   y = []
   y_err = []
   for i in range (0, N) :
       y.append ( f(x[i]) + e[i])
       y_err.append (abs (e[i])) #per rappresentare barre di errore l'errore non può essere negativo

#rappresentare i punti in un grafico con barre di errore
   plt.errorbar (x, y, yerr = y_err, xerr = 0., color = 'blue')
   plt.title ('punti pseudo casuali con errore gaussiano')
   plt.xlabel ('x')
   plt.ylabel ('y')
   plt.show()
   plt.clf ()

#a partire dalla funzione f_par attuare un fit del grafico precedente
#controllare se il fit ha avuto successo stampando a schermo Q^2 e p-value
#inserire informazioni in ingresso per migliorare la bontà del fit, utilizzando algoritmi basati sui 6 punti
   p0_stima = 0.5 * (max(y) - min(y)) # vedo p0 come l'ampiezza su y
   p1_stima = np.pi / (x[trova_max(y, N)]-x[trova_min(y, N)]) #semiampiezza su x pari a pi greco se p1=1
   p3_stima = mean (np.array(y)) #traslazione sulla verticale stimata con media delle y perchè con p3=0 la funzione sarebbe simmetrica rispesso asse x
   min_quadrati = LeastSquares (x, y, e, f_par )
   m = Minuit(min_quadrati, p0 = p0_stima, p1= p1_stima, p2 = 0., p3=p3_stima) 
   m.migrad ()
   Q_squared = m.fval 
   N_dof = m.ndof 
   p_value = 1 - chi2.cdf (Q_squared, N_dof)
   display (m) 
   print ('Q quadro per errori gaussiani:', Q_squared)
   print ('gradi di libertà:', N_dof)
   print ('p-value associato:', p_value)

#aggiungere un errore sistematico delta in tutti i punti
#stimare la nuova incertezza y_err_mod come la somma in quadratura di ei e delta
#rappresentare il nuovo insieme di punti con un grafico a barre di errore
   alpha = 1.5 
   e_sigma_mod = alpha * e_sigma
   y_mod = []
   y_err_mod = []
   sigma_y_mod = []
   for i in range (0, N) :
       y_err_mod.append(sqrt (rand_TCL_ms(0., e_sigma_mod)**2 + e[i]**2))
       sigma_y_mod.append(abs(y_err_mod[i])) #per rappresentare barre di errore l'errore non può essere negativo
       y_mod.append (f(x[i])+ y_err_mod[i])

   plt.errorbar (x, y_mod, yerr = sigma_y_mod, xerr = 0., color = 'blue')
   plt.title ('punti pseudo casuali con errore non noto')
   plt.xlabel ('x')
   plt.ylabel ('y')
   plt.show()
   plt.clf ()

#realizzare un nuovo fit del grafico 
   p0_stima_mod = 0.5 * (max(y_mod) - min(y_mod)) # vedo p0 come l'ampiezza su y
   p1_stima_mod = np.pi / (x[trova_max(y_mod, N)]-x[trova_min(y_mod, N)]) #semiampiezza su x pari a pi greco se p1=1
   p3_stima_mod = mean (np.array(y_mod)) #traslazione sulla verticale stimata con media delle y perchè con p3=0 la funzione sarebbe simmetrica rispesso asse x
   min_quadrati = LeastSquares (x, y_mod, y_err_mod, f_par )
   m_mod = Minuit(min_quadrati, p0 = p0_stima_mod, p1= p1_stima_mod, p2 = 0., p3=p3_stima_mod) 
   m_mod.migrad ()
   Q_squared_mod = m_mod.fval 
   N_dof_mod = m_mod.ndof 
   p_value_mod = 1 - chi2.cdf (Q_squared_mod, N_dof_mod)
   display (m_mod) 
   print ('Q quadro per errori non noti:', Q_squared_mod)
   print ('gradi di libertà:', N_dof_mod)
   print ('p-value associato:', p_value_mod)
   
#stimare l'incertezza sulle misure a partire dal valore di Q^2 (determinare errore a posteriori)
   scale_factor = sqrt (Q_squared_mod / N_dof)
   sigma = scale_factor * y_err_mod [0]
   print ('errore stimato a posteriori;', sigma)
#generare toy_experiments per verificare il funzionamento della tecnica
   N_toy = 1000
   Q_squared_toy = []
   for i in range (0, N_toy) :
      y_mod = []
      y_err_mod = []
      sigma_y_mod = []
      for i in range (0, N) :
          y_err_mod.append(sqrt (rand_TCL_ms(0., e_sigma_mod)**2 + e[i]**2))
          y_mod.append (f(x[i])+ y_err_mod[i])
      p0_stima_mod = 0.5 * (max(y_mod) - min(y_mod)) 
      p1_stima_mod = np.pi / (x[trova_max(y_mod, N)]-x[trova_min(y_mod, N)]) 
      p3_stima_mod = mean (np.array(y_mod)) 
      min_quadrati = LeastSquares (x, y_mod, y_err_mod, f_par )
      m_mod = Minuit(min_quadrati, p0 = p0_stima_mod, p1= p1_stima_mod, p2 = 0., p3=p3_stima_mod) 
      m_mod.migrad ()
      Q_squared_mod = m_mod.fval 
      Q_squared_toy.append (Q_squared_mod)

   Q_squared_mean = mean (Q_squared_toy)
   scale_factor = sqrt (Q_squared_mean / N_dof)
   sigma_mean = scale_factor * y_err_mod [0]
   print ('errore stimato a posteriori da toy experiments;', sigma_mean)


       
   

if __name__ == "__main__":
    main ()