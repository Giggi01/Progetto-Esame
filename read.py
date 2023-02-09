########################################################################
#                                                                      #
#  RIELABORAZIONE DATI PER OTTENERE FLUSSO DATI IN FUNZIONE DEL TEMPO  #
#                                                                      #
########################################################################

import pandas as pd
import os

# Definisco uno funzione che rielabori i dati


def read(data, save_to_file):  # l'argomento e' il file csv che si vuole rielaborare

    # Lettura del csv

    # legge file dalla directory dove si trova il csv (per ora il daily)
    file = pd.read_csv(data)

    #  Creo 2 liste vuote per l'intervallo di tempo e per il flusso di fotoni

    date = []  # lista vuota per tempo
    photon_flux = []  # lista vuota per flusso fotoni
    photon_flux_error = []  # lista vuota per errore flusso fotoni

    # Tramite un ciclo appendo i valori ai tre nuovi array

    for i in range(len(file["MET"])):
        # condizione per mettere l'errore a zero
        if file["Photon Flux Error(photons cm-2 s-1)"][i] == "-":
            # appendo zero alla lista degli errori
            photon_flux_error.append(0.0)
        else:
            # convreto la stringa in float
            new_photon_flux_error = float(
                file["Photon Flux Error(photons cm-2 s-1)"][i])
            # appendo il valore alla lista degli errori
            photon_flux_error.append(new_photon_flux_error)

    for i in range(len(file["MET"])):
        if file["TS"][i] < 4:  # condizione per cui photon_flux e' considerabile nulla

            new_photon_flux = 0.0 #float(
                #file["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"][i][2:])
            # appendo il photon flux alla lista del flusso di fotoni
            photon_flux.append(new_photon_flux)
            # leggo la data giuliana e sottraggo ogni elemento con il primo per ottenere una lista di tempo
            new_date = int(file["Julian Date"][i] - file["Julian Date"][0])
            # appendo la nuova data nella lista della data
            date.append(new_date)
        else:

            # converto in float il photon flux
            float_photon_flux = float(
                file["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"][i])
            # appendo il valore al nuovo array del flusso di fotoni
            photon_flux.append(float_photon_flux)
            new_date = int(file["Julian Date"][i] -
                           file["Julian Date"][0])  
            date.append(new_date)  

    #Creo la cartella dove voglio salvare i dati se richiesto 

    if os.path.isdir(os.path.join(os.path.splitext(data)[0]))==False:
        os.mkdir(os.path.join(os.path.splitext(data)[0]))
    
    if save_to_file:

        d = {'Tempo [d]' : date, 'Photon_Flux [Photon Flux [0.1-100 GeV](photons cm-2 s-1)]' : photon_flux,  'Photon Flux Error(photons cm-2 s-1)' : photon_flux_error}
        df = pd.DataFrame(data = d)
        df.to_csv(os.path.join(os.path.splitext(data)[0], 'Dati_segnale.txt'), index = False)

    # restituisce i due array rielaboarti
    return (date, photon_flux, photon_flux_error) 
