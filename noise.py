######################
#                    #
# ANALISI DEL RUMORE #
#                    #
##1###################

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

def noise(freq, pot, label, folder, save_to_file):

    # Definisco la funzione per riconoscere il tipo di rumore

    def f_noise(f, N, beta):

        # N : normalizzazione
        # f : frequenza
        # beta : esponente per dipendenza da frequenza

        return N/f**beta

    # Fit dei dati

    i = 2 # parametro per il fit dei dati (escludere i primi 2)

    if folder[len(folder)-11:len(folder)] == 'monthly.csv': # controllo per vedere se il file e' del campionamento mensile
        i = 3 # per i campionamenti mensili e' meglio eliminare i primi 3 dati

    params, params_covariance = optimize.curve_fit(
        f_noise, freq[i:len(freq)//2], pot[i:len(pot)//2],  maxfev=5000)
    if save_to_file:
        d = {'Normalizzazione': params[0], 'Varianza della normalizzazione': params_covariance[0,0], '$\beta$' : params[1], 'Varianza di $\beta$' : params_covariance[1,1]}
        df = pd.DataFrame(data = d, index = [0])
        df.to_csv(os.path.join(os.path.splitext(folder)[0], 'Dati_noise.txt'), index = False)
    else:
        print('Parameters Fit', params)
        print('Covariance', params_covariance[0,0], params_covariance[1,1])  # Stampo a schermo i valori del fit

    # Grafico con fit e visualizzazione dei valori

    label = os.path.splitext(label)[0]

    fig, ax = plt.subplots(figsize=(9, 6))
    plt.title('LAT Light Curve (noise)')
    plt.plot(freq[i:len(freq)//2],  pot[i:len(pot)//2], "o", label = label)
    plt.plot(freq[i:len(freq)//2], f_noise(freq[i:len(freq)//2],
             params[0], params[1]), color='red', label = "Noise fit")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('f $[Hz]$')
    plt.ylabel('$|c_{FFT}|^2$ [$ph^{2}$ $cm^{-4}$ $s^{-2}$]')
    plt.text(0.1, 0.1, r'Noise  -  $\beta$ = {:1.2f} $\pm$ {:1.2f}'.format(params[1], np.sqrt(
        params_covariance[1, 1])), fontsize=14, transform=ax.transAxes, color='black')
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Noise_fit_plot.png"))
    else:
        plt.show()
    plt.close(fig)

    return params, params_covariance
