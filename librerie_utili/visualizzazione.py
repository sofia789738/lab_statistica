import matplotlib.pyplot as plt
import numpy as np

#regola di sturges: modo utilizzato per calcolare in quanti bin dividere l'istogramma
def sturges (l) :
   return int(np.ceil( 1 + 3.322 * np.log(l)))
#______________________________________________________________________________________________________________

#disegnare istogramma dato un sample di dati contenuto in un file s
def hist_file(s) :
    with open (s) as input_file:
      sample = [float (x) for x in input_file.readlines()]
      xMin = min(sample)
      xMax = max(sample)
      n = len(sample)
      sturges = int(np.ceil( 1 + 3.322 * np.log(n)))
      fig, ax = plt.subplots (nrows=1, ncols=1)
      n_bins = sturges(n)
      bin_edges = np.linspace (xMin, xMax, n_bins)
      ax.hist (sample, bins = bin_edges, color = 'blue') 
      plt.show ()
#______________________________________________________________________________________________________________

#rappresentare dati in un istogramma
def hist (sample) :
   xMin = min(sample)
   xMax = max(sample)
   n = len(sample)
   fig, ax = plt.subplots (nrows=1, ncols=1)
   n_bins = sturges(n)
   bin_edges = np.linspace (xMin, xMax, n_bins)
   ax.hist (sample, bins = bin_edges, color = 'blue') 
   ax.set_title ('istogramma')
   ax.set_xlabel ('asse x')
   ax.set_ylabel ('asse y')

   sample_mean = sum(sample)/n
   vertical_limits = ax.get_ylim () #visualizzare asse verticare (ad esempio in orrispondenza del valore medio)
   ax.plot ([sample_mean, sample_mean], vertical_limits, color = 'red')

   y_value = 4
   orizontal_limits = ax.get_xlim () ##visualizzare asse orizzontale (ad esempio in orrispondenza di y=4)
   ax.plot ([y_value, y_value], orizontal_limits, color = 'red')

   plt.show()
#________________________________________________________________________________________________________________

#rappresentare graficamente funzione f
def grafico_ax () :
   x_coord = np.linspace (0, 2 * np.pi, 10_000) #estremi di x tra cui rappresentare f, quante x generare
   y_coord_1 = np.sin (x_coord) # f (esempio)
   fig, ax = plt.subplots (nrows=1, ncols=1)
   ax.plot (x_coord, y_coord_1, label='sin (x)')
   ax.set_title ('Comparing trigonometric functions', size=14)
   ax.set_xlabel ('x')
   ax.set_ylabel ('y')
   ax.legend () #rappresenta le etichette contenute in ax.plot
   plt.savefig ('drawing_.png')
   plt.show ()

def grafico_plt () :
   x = np.linspace(0, 2 * np.pi, 100) #estremi di x tra cui rapresentare f, scorrevolezza del disegno
   sin = np.sin(x)
   plt.plot (x, sin, label="sinx", color='yellow')
   plt.title ('trigonometrical functions')
   plt.xlabel ('x')
   plt.ylabel ('y')
   plt.legend ()
   plt.savefig ('drawing_.png')
   plt.show ()

#_______________________________________________________________________________________________________
#grafico con barre di errore
def grafico_error (x, y, x_err, y_err) :
   plt.errorbar (x, y, y_err, x_err, color = 'blue')
   plt.show()
   