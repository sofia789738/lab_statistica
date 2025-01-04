#Ripetere l'esercizio di adattamento per un andamento parabolico

import random
from iminuit import Minuit
from iminuit.cost import LeastSquares
from ex1 import rand_range_list, rand_TCL_ms
from funzione import f_2, f_parametrizzata_2

def main () :
    #genero dati utilizzando parametri noti (genero il campione simulato)
    sigma_epsilon = random.random()
    randlist_x = rand_range_list (0, 10, 10)
    randlist_y = []
    epsilons = []
    for i in range (0,10) :
        epsilons.append(rand_TCL_ms(0., sigma_epsilon))
    for i in range (0,10) :
        randlist_y.append(f_2(randlist_x[i]) + epsilons[i])
    sigma_y = [sigma_epsilon] * 10

    #ricavo i parametri che descrivono le coppie di punti del campione simulato (adattamento)
    minimi_quadrati = LeastSquares(randlist_x, randlist_y, sigma_y, f_parametrizzata_2) #genero Q^2 (funzione di costo)
    m = Minuit(minimi_quadrati, a = 0., b= 0., c = 0.) #ricerco i valori di a, b e c per cui la funzione di costo è minimizzata
    m.migrad () #trovo a, b e c
    m.hesse () #trovo le incertezza su a, b e c

    #stampo i parametri
    my_par = m.parameters #nomi
    my_val = m.values #valori
    my_err = m.errors #errori sui valori
    print(my_par[0],'=', my_val[0], '+/-', my_err[0])
    print(my_par[1],'=', my_val[1], '+/-', my_err[1])
    print(my_par[2],'=', my_val[2], '+/-', my_err[2])

    #calcolo e stampo caratteristiche di Q squared
    Q_squared = m.fval
    N_dof = m.ndof
    print ('value of the fit Q-squared', Q_squared)
    print ('value of the number of degrees of freedom', N_dof)

    #calcolo e stampo matrice di covarianza
    print (m.covariance)
    print ('variance of a:', m.covariance[0][0])
    print ('variance of b:', m.covariance[1][1])
    print ('variance of c:', m.covariance[2][2])
    print ('covariance of a and b:', m.covariance[1][0])
    print ('covariance of c and b:', m.covariance[2][1]) 
    print ('covariance of a and c:', m.covariance[2][0]) 

if __name__ == "__main__" :
    main()
