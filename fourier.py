########################
#                      #
#  ANALISI DI FOURIER  #
#                      #
########################

from scipy import fft
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd


def fourier(dati, tempo, label, folder, save_to_file):

    label = os.path.splitext(label)[0]

    dt = tempo[1] - tempo[0]  # intervallo temporale
    pho_fft = fft.fft(dati)  # Coefficienti FT
    pho_ps = np.absolute(pho_fft)**2  # Spettro di potenza
    pho_freq = fft.fftfreq(len(pho_fft), d=dt)  # Frequenze

    # riordino le frequenze e le potenze con fftshift per mettere in ordine [-fmax,+fmax]

    pho_ps_shift = fft.fftshift(pho_ps)
    pho_freq_shift = fft.fftshift(pho_freq)

    # Plot spettro di potenza

    figure = plt.subplots(figsize=(10, 7))
    plt.title('Power Spectrum')
    plt.plot(pho_freq_shift, pho_ps_shift, label = label)
    plt.ylabel("$|c_{FFT}|^2$ [$ph^{2}$ $cm^{-4}$ $s^{-2}$]", fontsize=14)
    plt.xlabel("f [$d^{-1}$]", fontsize=14)
    # plt.yscale("log")
    # plt.xscale("log")
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Power_Spectrum.png"))
    else:
        plt.show()
    plt.close(figure[0])

    # Grafico Spettro di Potenza per frequenze positive (escludendo anche il termine c(0) per f=0)

    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve (positive frequencies)')
    plt.plot(pho_freq[1:len(pho_fft)//2], pho_ps[1:len(pho_fft)//2], "o", label = label)
    plt.xscale('log')
    plt.xlabel('f [$d^{-1}$]',                  fontsize=14)
    plt.ylabel('$|c_{FFT}|^2$ [$ph^{2}$ $cm^{-4}$ $s^{-2}$]', fontsize=14)
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Power_Spectrum_(positive frequencies).png"))
    else:
        plt.show()
    plt.close(figure[0])
    

    # Grafico Spettro di Potenza log-log
    figure = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve (log-log)')
    plt.plot(pho_freq[1:len(pho_fft)//2], pho_ps[1:len(pho_fft)//2], "o", label = label)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('f [$d^{-1}$]',                  fontsize=14)
    plt.ylabel('$|c_{FFT}|^2$ [$ph^{2}$ $cm^{-4}$ $s^{-2}$]', fontsize=14)
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Power_Spectrum_(log-log).png"))
    else:
        plt.show()
    plt.close(figure[0])

    # Massimo spettro di potenza
    pho_ps_max = np.argmax(pho_ps[1:len(pho_ps)//2])+1
    if save_to_file:
        d = {'Massimo PS' : pho_ps[pho_ps_max], 'Massima Frequenza' : pho_freq[pho_ps_max], 'Massimo Periodo' : (int(1/pho_freq[pho_ps_max]))}
        df = pd.DataFrame(data = d, index = [0])
        df.to_csv(os.path.join(os.path.splitext(folder)[0], 'Massimi_Fourier.txt'), index = False)
    else:
        print('Massimo PS: {:} - Freq {:} - Periodo: {:d}'.format(
            pho_ps[pho_ps_max], pho_freq[pho_ps_max], (int(1/pho_freq[pho_ps_max]))))

    # Grafico Spettro di Potenza in funzione del periodo (1/freq) con massimo
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve (max value and period)')
    plt.plot(1/pho_freq[1:len(pho_fft)//2], pho_ps[1:len(pho_fft)//2],"o", label = label),
    plt.plot(1/pho_freq[pho_ps_max], pho_ps[pho_ps_max], 'o', label = 'Max value')
    plt.xscale('log')
    plt.yscale('log')
    plt.text(0.8, 0.2, 'T ~ {:d} days'.format(int(1/pho_freq[pho_ps_max])), transform=ax.transAxes, fontsize=14, color='black')
    plt.xlabel('T [$d$]',                       fontsize=14)
    plt.ylabel('$|c_{FFT}|^2$ [$ph^{2}$ $cm^{-4}$ $s^{-2}$]', fontsize=14)
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(folder)[0], "Power_Spectrum_(max_value_and_period).png"))
    else:
        plt.show()
    plt.close(fig)

    if save_to_file:
        d = {'Coefficienti di Fourieri [$|c_{FFT}|$]' : pho_fft, 'Frequenza [$d^{-1}$]' : pho_freq, 'Potenza [$|c_{FFT}|^2$]' : pho_ps}
        df = pd.DataFrame(data = d)
        df.to_csv(os.path.join(os.path.splitext(folder)[0], 'Dati_fourier.txt'), index = False) 

    return pho_fft, pho_freq, pho_ps
