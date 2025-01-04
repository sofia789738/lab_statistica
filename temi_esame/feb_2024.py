import math
import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from iminuit.cost import LeastSquares
from numeri_casuali import rand_range_list, generate_TCL_ms
from visualizzazione import sturges

#definire funzione phi (x, a, b, c) che traccia un andamento parabolico
#si disegni l'andamento di phi nell'intervallo (0, 10)

def phi (x, a, b, c) :
    return a + b*x + c*x*x

def main () :
    x_coord = np.linspace (0, 10, 1000)
    a = 3.
    b = 2.
    c = 1.
    y_coord = phi (x_coord, a, b, c)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.plot (x_coord, y_coord, color = 'red')
    ax.set_title ('andamento parabolico')
    ax.set_xlabel ('x')
    ax.set_ylabel ('phi(x)')

#generare N = 10 punti xi distrubuiti secondo una distribuzione uniforme 
#associare ad ogni xi una coordinata yi = phi(x) + ei
#ei generati con metodo TCL distrubuiti secondo una Gaussiana con mu=0 e sigma_y=10 
    N = 10
    mu = 0.
    sigma = 10.
    x = rand_range_list (-20, 20, N)
    e = generate_TCL_ms (mu, sigma, N)
    y = []
    for i in range (0, N) :
        y.append(phi(x[i], a, b, c)+ e[i])

#realizzare un fit della funzione phi sul campione prima generato
    sigma_y = e
    min_quadrati = LeastSquares (x, y, sigma_y, phi )
    m = Minuit(min_quadrati, a = 0., b= 0., c = 0.) 
    m.migrad () 
    m.hesse ()
    my_par = m.parameters
    my_val = m.values
    my_err = m.errors
    print(my_par[0],'=', my_val[0], '+/-', my_err[0])
    print(my_par[1],'=', my_val[1], '+/-', my_err[1])
    print(my_par[2],'=', my_val[2], '+/-', my_err[2])

#costruire una distribuzione di Q^2 a partire dal fit effettuato, ripendolo usando toy_esperiments
    Q_squared = []
    N_toy = 10000
    #ottengo N-toy valori di Q_squared
    for i in range (0, N_toy) :
        x = rand_range_list (-20, 20, N)
        e = generate_TCL_ms (mu, sigma, N)
        y = []
        for i in range (0, N) :
           y.append(phi(x[i], a, b, c)+ e[i])
        min_quadrati = LeastSquares (x, y, e, phi )
        m_toy = Minuit(min_quadrati, a = 0., b= 1., c = 1.) 
        m_toy.migrad () 
        Q_squared.append(m_toy.fval)
  
#svolgere i punti precedenti con ei distribuiti uniformemente con sigma_y = 10
    sigma = 10.
    xf = sigma*math.sqrt(12/4) #dalla formula della varianza per una distribuzione uniforme
    xi = -xf
    Q_squared_mod = []
    for i in range (0, N_toy) :
        x = rand_range_list (-20, 20, N)
        e = rand_range_list (xi, xf, N)
        y = []
        for i in range (0, N) :
           y.append(phi(x[i], a, b, c)+ e[i])
        min_quadrati_mod = LeastSquares (x, y, e, phi )
        m_toy_mod = Minuit(min_quadrati_mod, a = 0., b= 1., c = 1.) 
        m_toy_mod.migrad () 
        Q_squared_mod.append(m_toy.fval)

#disegnare la distribuzione di Q_squared così ottenuta sovrapposta alla precedente
    xMin = min(Q_squared + Q_squared_mod)
    xMax = max(Q_squared + Q_squared_mod)
    n_bins = sturges(N_toy)
    bin_edges = np.linspace (xMin, xMax, n_bins)
    fig, ax = plt.subplots (nrows=1, ncols=1)
    ax.hist (Q_squared, bins = bin_edges, label = 'sigma_y gaussiani', color = 'blue', histtype = 'step') 
    ax.hist (Q_squared_mod, bins = bin_edges, label = 'sigma_y uniformi', color = 'green', histtype = 'step') 
    ax.set_title ('distribuzione di Q_squared')
    ax.legend ()
    ax.set_xlabel ('Q^2')
    ax.set_ylabel ('conteggi')
    plt.show ()

#a partire dalla distribuzione di Q^2 determinare la soglia oltre cui rigettare il risultato del fit (dato Q^2)
#ricercare p-value > 0,1
    alpha = 0.1
    Q_squared.sort ()
    soglia = math.floor(N_toy * (1-alpha))
    Q2_soglia = Q_squared [soglia] #trovo l'elemento che sta al 9000esimo posto (prima devo riordinare Q_squared)
    print ('valore di soglia=', Q2_soglia)

if __name__ == "__main__":
    main ()