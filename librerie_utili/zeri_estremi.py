import math

#trovare ZERO di una funzione con il metodo di bisezione
#con ciclo while
def bisection (xmin, xmax, g, prec=0.0001) :
    av = xmin
    while (xmax-xmin > prec) :
        av = (xmax+xmin)/2
        fmedia = g(av)
        if fmedia == 0 :
            return av
        if g(xmin) * fmedia > 0. :
            xmin = av 
        else :
            xmax = av
    return av

#con funzione ricorsiva
def recursive_bisection (xmin, xmax, g, prec=0.0001) :
    av = (xmin+xmax)/2
    if (xmax-xmin)<prec :
       return av
    if g(xmin) * g(av) > 0. :
       return recursive_bisection (av, xmax, g, prec=0.0001)
    else :
       return recursive_bisection (xmin, av, g, prec=0.0001)
#____________________________________________________________________________________________________________

#determinare il MINIMO di una funzione con l'algoritmo della sezione aurea, in un intervallo tra xmin e xmax
#ciclo while
def golden_ratio (xmin, xmax, g, prec=0.001):
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    while (xmax-xmin) > prec :
        if g(xi) > g (xf) :
           xmin = xi
           xi = xf
           xf = xmin + r*(xmax-xmin)
        else :
           xmax = xf
           xf = xi
           xi = xmin + (1-r)*(xmax-xmin)   
    return (xmax+xmin)/2

#funzione ricorsiva
def rec_golden_ratio (xmin, xmax, g, prec=0.001):
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    if xmax-xmin < prec :
        return (xmax+xmin)/2
    if g(xi) > g (xf) :
        return rec_golden_ratio(xi, xmax, g, prec=0.001)
    else :
        return rec_golden_ratio(xmin, xf, g, prec=0.001)
#_____________________________________________________________________________________________________________
    
#determinare il MASSIMO di una funzione con l'algoritmo della sezione aurea, in un intervallo tra xmin e xmax
#ciclo while
def golden_ratio_max_LL(xmin, xmax, g, prec=0.001) :
    r = (math.sqrt(5)-1)/2
    xf = xmin + r*(xmax-xmin)
    xi = xmin + (1-r)*(xmax-xmin)
    while (xmax-xmin) > prec :
        if g(xf) > g (xi) :
           xmin = xi
        else :
           xmax = xf 
        xf = xmin + r*(xmax-xmin)
        xi = xmin + (1-r)*(xmax-xmin)
    x = (xmax+xmin)/2.   
    return x
