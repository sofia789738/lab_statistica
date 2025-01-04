import random
from math import sqrt
import numpy as np

#algoritmo per generari numeri casuali tra 0 e M tramite la funzione x_n+1 = A*x_n + C
#seed rappresenta il seme ed è 0 (per avere xmin=0), tot è il numero totale di numeri casuali da generare
def rand(tot, seed) :
    sequence = []
    x = seed
    M = 2147483647
    A = 214013
    C = 2531011
    for i in range (0, tot) :
        x = (A*x + C) % M
        sequence.append(x)
    return sequence
#__________________________________________________________________________________________________________

#generare un sequenza di tot numeri casuali in un range tra min e max
#numeri distribuiti con distribuzione uniforme
def rand_range_list (min, max, tot) :
    randlist = []
    for i in range (0,tot) :
         x = min + (max-min)*random.random()
         randlist.append (x)
    return randlist

#generare un numero casuale tra min e max
def rand_range (min, max) :
         x = min + (max-min)*random.random()
         return x
#__________________________________________________________________________________________________________

#generare un numero casuale con il metodo try and catch
#f può essere scritta come una python-funzione
#xmin e xmax sono il valore max e min che il numero casuale può assumere mentre ymax è il limite di f(x)
#x distribuite con pdf = f
def rand_TAC (f, xMin, xMax, yMax) :
    x = rand_range (xMin, xMax)
    y = rand_range (0, yMax)
    while (y > f (x)) :
        x = rand_range (xMin, xMax)
        y = rand_range (0, yMax)
    return x

#generare N numeri casuali con il metodo TAC
#numeri casuali distribuiti in modo proporzionale all'area sotto la pdf (f)
def generate_TAC (f, xMin, xMax, yMax, N, seed = 0.) :
    if seed != 0. : random.seed (float (seed)) 
    randlist = []
    for i in range (N):
            randlist.append (rand_TAC (f, xMin, xMax, yMax))
    return randlist
#__________________________________________________________________________________________________________

#generare n_tot numeri casuali con il metodo della funzione inversa
#inumeri generati seguono una distribuzione di probabilità esponenziale
def generate_exp (n_tot, tau_t) :
    exp_randlist = []
    for i in range (0, n_tot) : 
        y = random.random()
        x = -tau_t * np.log(1-y)
        exp_randlist.append(x)
    return exp_randlist

#generare un numero casuale avente pdf esponenziale
def exp_random (tau) :
    return -tau*np.log(1-random.random())
#__________________________________________________________________________________________________________

#generare un numero casuale avente distribuzione di probabilità gaussiana in un intervallo tra xmin e xmax
#metodo del teorema centrale del limite 
def TCL_random (seed, xmin, xmax, tot) :
    sum = seed
    for i in range (0, tot) :
        x = xmin + (xmax-xmin) * random.random()
        sum = sum + x
    average = sum / tot
    return average

#generare N eventi casuali con distribuzione di probabilità gaussiana
def generate_TCL (xMin, xMax, N, N_sum = 10, seed = 0.) :
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append (TCL_random (0., xMin, xMax, N_sum))
    return randlist

#generare un numero pseudo-casuale con il metodo del teorema centrale del limite, note media e sigma della gaussiana
def rand_TCL_ms (mean, sigma, N_sum = 10) :
    y = 0.
    delta = sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum 
    return y 

#generare N numeri pseudo-casuali con il metodo del teorema centrale del limite
#note media e sigma della gaussiana, a partire da un determinato seed 
def generate_TCL_ms (mean, sigma, N, N_sum = 10, seed = 0.) :
    if seed != 0. : random.seed (float (seed))
    randlist = []
    delta = sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N):
        randlist.append (TCL_random (0., xMin, xMax, N_sum))
    return randlist
#__________________________________________________________________________________________________________


