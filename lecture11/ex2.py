#Utilizzare la iMinuitlibreria per eseguire un adattamento sul campione simulato.
#Controllare se l'adattamento è riuscito.
#Stampare sullo schermo i valori dei parametri determinati e i loro sigma.

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

    #controllo l'adattamento
    is_valid = m.valid
    print ('success of the fit: ', is_valid)

    #stampo i parametri
    my_par = m.parameters #nomi
    my_val = m.values #valori
    my_err = m.errors #errori sui valori
    print(my_par[0],'=', my_val[0], '+/-', my_err[0])
    print(my_par[1],'=', my_val[1], '+/-', my_err[1])

if __name__ == "__main__" :
    main()