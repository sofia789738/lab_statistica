
from visualizzazione import sturges
from numeri_casuali import generate_TCL_ms
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
from iminuit import Minuit
from iminuit.cost import LeastSquares
from IPython.display import display

#generare 4 coppie (xi, yi) di punti pesudo casuali legati dalla relazione f
#yi distribuito attorno f(xi) con pdf gaussiana
#e_yi generati usando il teorema centrale del limite, prendendo come parametri in ingresso mean e sigma

def f (x) :
    return (x-2)**3 + 3

def f_parametrizzata (x, p0, p1) :
    return (x-p0)**3 + p1

def g_parametrizzata (x, p0, p1) :
    return (x-p0)**2 + p1

def fit (x, y, yerr, f_par) :
    min_quadrati = LeastSquares (x, y, yerr, f_par)
    m = Minuit(min_quadrati, p0 = 0., p1 = 0.) 
    m.migrad ()
    Q_squared = m.fval 
    df = m.ndof 
    p_value = 1 - chi2.cdf (Q_squared, df)
    return Q_squared, p_value

def main () :
    N = 4
    x = [0.5, 1.5, 2.5, 3.5]
    y = []
    sigma = 0.2
    mean = 0.
    e = generate_TCL_ms (mean, sigma, N)
    y_err = []
    for i in range (0, N) :
        y.append (f(x[i])+e[i])
        y_err.append (abs(e[i])) #per rappresentare errorbar servono errori positivi
    

#rappresentare punti generati con barre di errore
    plt.errorbar (x, y, yerr = y_err, color = 'blue')
    plt.title ('coppie di punti pseudo-casuali')
    plt.xlabel ('x')
    plt.ylabel ('y')
    plt.show()

#dopo aver definito f_parametrizzata eseguire il fit dei dati generati (determinando t0, t1)
#stampare a schermo il valore di q^2 e p-value corrispondenti
    min_quadrati = LeastSquares (x, y, e, f_parametrizzata)
    m = Minuit(min_quadrati, p0 = 0., p1 = 0.) 
    m.migrad ()
    display (m)
    Q_squared = m.fval 
    df = m.ndof 
    p_value = 1 - chi2.cdf (Q_squared, df)
    print ('Q-squared:', Q_squared)
    print ('gradi di libertà:', df)
    print ('p-value associato:', p_value)
    
#utilizzando un ciclo produrre N_toy experiment come per il punto precedente
    Q_2 = []
    p = []
    N_toy = 1000
    for i in range (0, N_toy) :
        y = []
        e = generate_TCL_ms (mean, sigma, N)
        y_err = []
        for i in range (0, N) :
           y.append (f(x[i])+e[i])
        Qsquared, pvalue = fit (x, y, e, f_parametrizzata)
        Q_2.append (Qsquared)
        p.append (pvalue)
#riempire due istogrammi con i valori di Q_squared e p-value
    xMin = min(Q_2)
    xMax = max(Q_2)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N_toy)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (Q_2, bins = bin_edges, color = 'pink') 
    ax.set_title ('adattamento con f')
    ax.set_xlabel ('Q squared')
    ax.set_ylabel ('conteggi')
    plt.show ()

    xMin = min(p)
    xMax = max(p)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N_toy)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (p, bins = bin_edges, density = True, color = 'pink') 
    ax.set_xlabel ('p-value')
    ax.set_ylabel ('conteggi')
    plt.show ()

#generare coppie di numeri casuali come prima ma usare una diversa funzione per il fit
    Q_2_mod = []
    for i in range (0, N_toy) :
        y = []
        e = generate_TCL_ms (mean, sigma, N)
        y_err = []
        for i in range (0, N) :
           y.append (f(x[i])+e[i])
        Qsquared_mod, pvalue_mod = fit (x, y, e, g_parametrizzata)
        Q_2_mod.append (Qsquared_mod)
#raccogliere in un istogramma i valori di Q_squared per N_toy experiments
    xMin = min(Q_2_mod)
    xMax = max(Q_2_mod)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    n_bins = sturges(N_toy)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    ax.hist (Q_2_mod, bins = bin_edges, density = True, color = 'pink') 
    ax.set_title ('adattamento con g')
    ax.set_xlabel ('Q squared')
    ax.set_ylabel ('conteggi')
    plt.show ()
    
if __name__ == "__main__":
    main ()


