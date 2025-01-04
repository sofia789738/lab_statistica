#Calcola il valore di Q^2 utilizzando i punti e la funzione approssimata ottenuti nell'esercizio precedente.
#Confrontare il valore ottenuto con iminuitquello calcolato.

#Stampa il valore dei gradi di libertà dell'adattamento.

#Aggiungere la stampa dell'intera matrice di covarianza dei parametri di adattamento.

import random
from iminuit import Minuit
from iminuit.cost import LeastSquares
from ex1 import rand_range_list, rand_TCL_ms
from funzione import f, f_parametrizzata

def main () :
    #genero dati utilizzando parametri noti (genero il campione simulato)
    sigma_epsilon = random.random()
    randlist_x = rand_range_list (0, 10, 10)
    randlist_y = []
    epsilons = []
    for i in range (0,10) :
        epsilons.append(rand_TCL_ms(0., sigma_epsilon))
    for i in range (0,10) :
        randlist_y.append(f(randlist_x[i]) + epsilons[i])
    sigma_y = [sigma_epsilon] * 10

    #ricavo i parametri che descrivono le coppie di punti del campione simulato (adattamento)
    minimi_quadrati = LeastSquares(randlist_x, randlist_y, sigma_y, f_parametrizzata) #genero Q^2 (funzione di costo)
    m = Minuit(minimi_quadrati, m = 0., q= 0.) #ricerco i valori di q e m per cui la funzione di costo è minimizzata
    m.migrad () #trovo m e q
    m.hesse () #trovo le incertezza su p e q
    m_fit = m.values[0]
    q_fit = m.values[1]

    #calcolo Q^2 con i due metodi e confronto
    Q_squared_fit = m.fval
    Q_squared_points = 0.
    for i in range (0, 10):
        Q_squared_points = Q_squared_points + ((randlist_y[i] - f_parametrizzata(randlist_x[i], m_fit, q_fit))/ sigma_y[i]) **2 #considero stesso errore per tutti i punti
                                                                                                                                #uso i parametri calcolati minimizzando Q^2
    Q_squared_diff = abs(Q_squared_fit - Q_squared_points)                                                                                                         
    print ('value of the fit Q-squared', Q_squared_fit)
    print ('value of Q squared calculated', Q_squared_points)
    print ('difference', Q_squared_diff)

    #calcolo e stampo gradi di libertà
    N_dof = m.ndof
    print ('value of the number of degrees of freedom', N_dof)

    #calcolo e stampo matrice di covarianza
    print (m.covariance)
    print ('variance of m:', m.covariance[0][0])
    print ('variance of q:', m.covariance[1][1])
    print ('covariance:', m.covariance[1][0]) #matrice simmetrica

if __name__ == "__main__" :
    main()

    