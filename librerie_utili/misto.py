from numeri_casuali import rand_range
import numpy as np
from scipy.integrate import quad

#PROGRAMMAZIONE FUNZIONALE:
#The built-in MAP function applies a passed-in function to all elements of a list
#squared is a new list containing the square of the elements of lista
lista = list (range (-5, 5))
squared = list (map (lambda x : x*x, lista))
#the built-in FILTER function applies a passed-in function to all elements of a list and returns 
#a list with the items for which the function is True:
lista = list (filter (lambda x: x % 2 == 0, range(-5, 5)))
#_______________________________________________________________________________________________

#calcolare l'integrale di una data funzione su intervalli finiti
def int_finito (f, xmin, xmax) :
    area = quad (f, xmin, xmax)
    val_area = area[0] #valore integrale
    err_area = area[1] #stima dell'errore assoluto sull'integrale
    return val_area, err_area 

#calcolare l'integrale di una data funzione su intervalli infiniti
def int_più_infinito (f, xmin) :
    area = quad (f, xmin, np.inf)
    val_area = area[0] 
    err_area = area[1] 
    return val_area, err_area 

def int_meno_infinito (f, xmax) :
    area = quad (f, -1*np.inf, xmax)
    val_area = area[0] 
    err_area = area[1] 
    return val_area, err_area 
#_______________________________________________________________________________________________

#calcolare area sottesa (integrale) da una funzione con il metodo hit or miss
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
