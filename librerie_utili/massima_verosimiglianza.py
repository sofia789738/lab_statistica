import numpy as np
import math

#theta può essere uno o più parametri

#verosimiglianza
def likelihood (randlist, pdf, theta) :
    L = 1.
    sample = np.array (randlist)
    for x in sample :
        L = L * pdf (x, theta)
    return L

#logaritmo della verosimiglianza
def log_likelihood (theta, pdf, sample) :
       logL = 0.
       for x in sample:
          if (pdf (x, theta) > 0.) : 
              logL = logL + np.log (pdf (x, theta))    
       return logL

#logaritmo del rapporto tra la funzione di verosimiglianza e il suo valore massimo
def loglikelihood_ratio (theta, pdf, sample, theta_hat) :
    l = 0.
    sample = np.array (sample)
    for x in sample :
         l = l + np.log (pdf (x, theta)) - np.log(pdf(x, theta_hat))
    return l 

#trovare il massimo di loglikelihood
#algoritmo della sezione aurea assumendo theta compreso tra xmax e xmin
def golden_ratio_max_LL(xmin, xmax, log_likelihood, randlist, pdf, prec=0.0001) :
      g = lambda theta : log_likelihood (theta, pdf, randlist)
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
      mean_hat = (xmax+xmin)/2.   
      return mean_hat

#___________________________________________________________________________________
#trovare l'incertezza sul valore di theta utilizzando il metodo grafico
#metodo di bisezione per trovare i due punti (theta - σ) e (theta + σ)
def intersect_LLR (
    g,              # funzione di cui trovare lo zero
    pdf,            # probability density function of the events
    sample,         # sample of the events
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo 
    ylevel,         # value of the horizontal intersection    
    theta_hat,      # maximum of the likelihood    
    prec = 0.0001): # precisione della funzione        

    def gprime (x) :
        return g (x, pdf, sample, theta_hat) - ylevel

    xAve = xMin 
    while ((xMax - xMin) > prec) :
        xAve = 0.5 * (xMax + xMin) 
        if (gprime (xAve) * gprime (xMin) > 0.) : xMin = xAve 
        else                                    : xMax = xAve 
    return xAve 

def intervallo_confidenza (xmin, xmax, sample, pdf, log_likelihood) :
    theta_hat = golden_ratio_max_LL (xmin, xmax, log_likelihood, sample, pdf, prec = 0.0001)    
    theta_hat_minusS = intersect_LLR (loglikelihood_ratio, pdf, sample, xmin, theta_hat, -0.5, theta_hat)
    theta_hat_plusS = intersect_LLR (loglikelihood_ratio, pdf, sample, theta_hat, xmax, -0.5, theta_hat)
    return theta_hat_minusS, theta_hat_plusS

