from iminuit import Minuit
from iminuit.cost import LeastSquares, UnbinnedNLL, ExtendedBinnedNLL
from IPython.display import display
import numpy as np
from scipy.stats import norm, chi2
from visualizzazione import sturges

#trovare parametri che descrivono un modello lineare f_modello
#esempio in cui f_modello è una parabola (determinare a, b, c)
#y con errore sigma_y, errore sulle x trascurabili (nullo)
def least_squares_lineare (x, y, sigma_y, f_modello) :
    min_quadrati = LeastSquares (x, y, sigma_y, f_modello )
    m = Minuit(min_quadrati, a = 0., b= 0., c = 0.) 
    m.migrad () #trovo parametri
    m.hesse () #trovo le incertezze sui parametri
    my_par = m.parameters #nomi
    my_val = m.values #valori
    my_err = m.errors #errori sui valori
    Q_squared = m.fval #valore di Q^2 associato al fit
    N_dof = m.ndof #numero di gradi di libertà
    covariance = m.covariance #matrice di covarianza
    colleration = m.covariance.correlation () #matrice di correlazione dei parametri
    display (m) #output sullo schermo del fit, riassume tutte le informazioni sopra
    p_value = 1 - chi2.cdf (Q_squared, N_dof) #per determinare la bontà del fit
                                              #Q^2 distribuito come un chi quadro se i sigma_y sono distribuiti con pdf gaussiana
    print ('Q quadro:', Q_squared)
    print ('gradi di libertà:', N_dof)
    print ('p-value associato:', p_value)

#trovare parametri che descrivono un modello di istogramma ist_modello
#y con errore sigma_y, errore sulle x trascurabili (nullo)
def least_squares_ist (sample) :
    n = len(sample)
    n_bins = sturges(n)
    bin_content, bin_edges = np.histogram (sample, bins=n_bins)
    bin_centres = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    
#trovare parametri che descrivono la pdf di un evento x
#ipotesi : eventi xi distribuiti gaussianamente
def maximum_likelihood_unb (sample) :
    def modello_unb (x, mu, sigma) :
        return norm.pdf(x, mu, sigma)
    f_costo_unb = UnbinnedNLL (sample, modello_unb)
    mean = np.mean(sample) #stimo parametri per suggeririre a Minuit circa dove cercare mu e sigma
    dev = np.std(sample)
    my_minuit_unb = Minuit (f_costo_unb, mu = mean, sigma = dev)
    my_minuit_unb.limits["sigma"] = (0, None) #deviazione standard necessariamente positiva
    my_minuit_unb.migrad () 
    my_par = my_minuit_unb.parameters #nomi
    my_val = my_minuit_unb.values #valori
    my_err = my_minuit_unb.errors #errori sui valori
    Q_squared = my_minuit_unb.fval #valore di Q^2 associato al fit
    N_dof = my_minuit_unb.ndof #numero di gradi di libertà
    covariance = my_minuit_unb.covariance #matrice di covarianza
    colleration = my_minuit_unb.covariance.correlation () #matrice di correlazione dei parametri
    display (my_minuit_unb) 

#trovare paramentri che descrivono una distribuzione binnata 
#ipotesi : eventi xi distribuiti gaussianamente
def maximum_likelihood_bin (sample) :
    n = len(sample)
    n_bins = sturges(n)
    bin_content, bin_edges = np.histogram (sample, bins=n_bins)
    mean = np.mean(sample) #stimo parametri per suggeririre a Minuit circa dove cercare mu e sigma
    dev = np.std(sample)
    def modello_bin (bin_edges, N_tot, mu, sigma) : #attenzione all'ordine: prima la variabile poi i parametri 
         return N_tot * norm.cdf (bin_edges, mu, sigma)
    f_costo_bin = ExtendedBinnedNLL(bin_content, bin_edges, modello_bin)
    my_minuit_bin = Minuit(f_costo_bin, N_tot = n, mu = mean, sigma = dev)
    my_minuit_bin.limits["N_tot", "sigma"] = (0, None) #deviazione standard e numero totale di eventi necessariamente positivi
    my_minuit_bin.migrad ()
    Q_squared = my_minuit_bin.fval #valore di Q^2 associato al fit
    N_dof = my_minuit_bin.ndof #numero di gradi di libertà
    display (my_minuit_bin)
    p_value = 1 - chi2.cdf (Q_squared, N_dof) #per determinare la bontà del fit
                                              #Q^2 distribuito come un chi quadro se i bin-content sono distribuiti con pdf gaussiana
                                              #vale se il numero di eventi è sufficientemente alto e quindi si hanno abbastanza misure per bin
 
 #stima dell'errore a posteriori

    
