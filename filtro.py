####################################################################
#                                                                  #
# APPLICO UN FILTRO IN FREQUENZA PER ANALIZZARE SOLO LUNGO PERIODO #
#                                                                  #
####################################################################

import numpy as np
from scipy import fft
import matplotlib.pyplot as plt
import os 
import pandas as pd


def filter(freq, ft, tempo, photons_flux, label, folder, save_to_file):

    # Determino i filtri da applicare alle frequenze in valore assoluto (0.5*10^-2, 0.2*10^-2, 0.1*10^-2)

    filtered_mask05 = np.absolute(freq) > 0.5e-2
    filtered_mask1 = np.absolute(freq) > 0.2e-2
    filtered_mask2 = np.absolute(freq) > 0.1e-2

    # Faccio una copia dei coefficienti di Fourier per poi applicare la maschera

    filtered_fft05 = ft.copy()
    filtered_fft02 = ft.copy()
    filtered_fft01 = ft.copy()

    filtered_fft05[filtered_mask05] = 0  # pongo a zero le freq superiori a fcut
    filtered_fft02[filtered_mask1] = 0  # pongo a zero le freq superiori a fcut
    filtered_fft01[filtered_mask2] = 0  # pongo a zero le freq superiori a fcut

    # Applico la trasformata invera per ottenre il segnale filtrato

    filtered_LC05 = (fft.ifft(filtered_fft05)).astype(float)
    filtered_LC02 = (fft.ifft(filtered_fft02)).astype(float)
    filtered_LC01 = (fft.ifft(filtered_fft01)).astype(float)

    # print(filtered_LC05)
    # print(filtered_LC1)
    # print(filtered_LC2)

    # Grafico di confronto tra segnale originale e segnale filtrato
    
    label = os.path.splitext(label)[0]

    # Caso filto per fcut = 0.5*10^-2

    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve')
    plt.plot(tempo, photons_flux, color='gray',  label=label)
    plt.plot(tempo, filtered_LC05,     color='red',        lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.5e-2)))
    plt.legend()
    plt.xlabel('Time [d]')
    plt.ylabel(r'Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)')
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Plot_segnale_filtrato_05.png"))
    else:
        plt.show()
    plt.close(figure[0])

    # Caso filto per fcut = 0.2*10^-2

    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve')
    plt.plot(tempo, photons_flux, color='gray',  label=label)
    plt.plot(tempo, filtered_LC02,     color='darkorange',        lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.2e-2)))
    plt.legend()
    plt.xlabel('Time [d]')
    plt.ylabel(r'Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)')
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Plot_segnale_filtrato_02.png"))
    else:
        plt.show()
    plt.close(figure[0])

    # Caso filto per fcut = 0.1*10^-2


    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve')
    plt.plot(tempo, photons_flux, color='gray',  label=label)
    plt.plot(tempo, filtered_LC01,     color='purple',        lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.1e-2)))
    plt.legend()
    plt.xlabel('Time [d]')
    plt.ylabel(r'Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)')
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Plot_segnale_filtrato_01.png"))
    else:
        plt.show()
    plt.close(figure[0])


    # Grafico con tutti i segnali filtrati e segnale originale

    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve')
    plt.plot(tempo, photons_flux, color='gray',  label=label)
    plt.plot(tempo, filtered_LC05,     color='red',        lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.5e-2)))
    plt.plot(tempo, filtered_LC02,     color='darkorange', lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.2e-2)))
    plt.plot(tempo, filtered_LC01,    color='purple',     lw=3,
             label=r'Light curve filtered $\nu$ < 1/{:d} d'.format(int(1/0.1e-2)))

    plt.legend()
    # plt.yscale('log')
    plt.xlabel('Time [d]')
    plt.ylabel(r'Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)')
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Plot_segnali_filtrati_all.png"))
    else:
        plt.show()
    plt.close(figure[0])

    if save_to_file:
        d = {'Coefficienti filtrati [$\nu$ < 1/ 200 d]' : filtered_fft05, 'Coefficienti filtrati [$\nu$ < 1/ 500 d]' : filtered_fft02 , 'Coefficienti filtrati [$\nu$ < 1/ 1000 d]' : filtered_fft01, 'Segnale filtrato [$\nu$ < 1/ 200 d]' : filtered_LC05,  'Segnale filtrato[$\nu$ < 1/ 500 d]' : filtered_LC02, 'Segnale filtrato [$\nu$ < 1/ 1000 d]' : filtered_LC01}
        df = pd.DataFrame(data = d)
        df.to_csv(os.path.join(os.path.splitext(folder)[0], 'Dati_segnali_filtarti.txt'), index = False) 

    return filtered_LC05, filtered_LC02, filtered_LC01
