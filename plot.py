########################
#                      #
#  GRAFICO DATI-TEMPO  #
#                      #
########################

import matplotlib.pyplot as plt
import os

def plot(time, dati, error_dati, label, folder, save_to_file):

    label = os.path.splitext(label)[0]

    figure = plt.subplots(figsize=(10, 7))
    plt.title("LAT Light Curve")
    plt.errorbar(time, dati, yerr=error_dati, fmt="o-",
                 label=label, ecolor='black')
    plt.xlabel("Time [d]", fontsize=14)
    plt.ylabel("Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)", fontsize=14)
    #plt.yscale("log")
    plt.legend()
    if save_to_file:
        plt.savefig(os.path.join(os.path.splitext(
            folder)[0], "Plot_segnale.png"))
    else:
        plt.show()
    plt.close(figure[0])
