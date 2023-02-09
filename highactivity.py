################################
#                              #
#  IDENTIFICO LE ALTE ATTIVITA #
#                              #
################################   
 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Le soglie dipendono dal tipo di sorgente analizzata quindi le differenzio
def soglia(label):

    soglia = 0  # valore iniziale per definire la variabile soglia
    if label == '4FGL J1224.9+2122 LCR':
        soglia = 0.6e-6   # Soglia minima di flusso per alte attivita
    elif label == '4FGL J1256.1-0547 LCR':
        soglia = 1.8e-6   # Soglia minima di flusso per alte attivita 
    elif label == '4FGL J1427.9-4206 LCR':
        soglia = 1.3e-6   # Soglia minima di flusso per alte attivita
    elif label == '4FGL J2232.6+1143 LCR':
        soglia = 1.85e-6   # Soglia minima di flusso per alte attivita
    elif label == '4FGL J2253.9+1609 LCR':
        soglia = 4.8e-6   # Soglia minima di flusso per alte attivita
    return soglia


# funzione che restituisce numero di alte attivita e le loro durata (calcolate a priori dai dati) in base alla sorgente
# 
def alta_attivita(label):
    n_high_act = 0
    len_high_act = []
    if label == '4FGL J1224.9+2122 LCR':
        n_high_act = 3
        len_high_act.append(532) 
        len_high_act.append(251)
        len_high_act.append(28)
    elif label == '4FGL J1256.1-0547 LCR':
        n_high_act = 4
        len_high_act.append(350) 
        len_high_act.append(28)
        len_high_act.append(182)
        len_high_act.append(210) 
    elif label == '4FGL J1427.9-4206 LCR':
        n_high_act = 3 
        len_high_act.append(7) 
        len_high_act.append(259)
        len_high_act.append(182)
    elif label == '4FGL J2232.6+1143 LCR':
        n_high_act = 4
        len_high_act.append(14) 
        len_high_act.append(98)
        len_high_act.append(336)
        len_high_act.append(56) 
    elif label == '4FGL J2253.9+1609 LCR':
        n_high_act = 6
        len_high_act.append(56) 
        len_high_act.append(35)
        len_high_act.append(84)
        len_high_act.append(49) 
        len_high_act.append(49) 
        len_high_act.append(7)

    return n_high_act, len_high_act

def line_high_activity(label):
    indici_x = []  # indici per tracciare linee delle varie alte attivita
    if label == '4FGL J1224.9+2122 LCR':
        indici_x.append(57)
        indici_x.append(141)
        indici_x.append(257)
        indici_x.append(301)
        indici_x.append(323)
        indici_x.append(335)
    elif label == '4FGL J1256.1-0547 LCR':
        indici_x.append(276)
        indici_x.append(334)
        indici_x.append(354)
        indici_x.append(366)
        indici_x.append(446)
        indici_x.append(480)
        indici_x.append(487)
        indici_x.append(525)        
    elif label == '4FGL J1427.9-4206 LCR':
        indici_x.append(88)
        indici_x.append(97)
        indici_x.append(217)
        indici_x.append(262)
        indici_x.append(713)
        indici_x.append(741)
    elif label == '4FGL J2232.6+1143 LCR':
        indici_x.append(213)
        indici_x.append(223)
        indici_x.append(383)
        indici_x.append(405)
        indici_x.append(418)
        indici_x.append(470)
        indici_x.append(485)
        indici_x.append(501)    
    elif label == '4FGL J2253.9+1609 LCR':
        indici_x.append(66)
        indici_x.append(82)
        indici_x.append(84)
        indici_x.append(97)
        indici_x.append(114)
        indici_x.append(134)
        indici_x.append(303)
        indici_x.append(318)
        indici_x.append(358)
        indici_x.append(373)
        indici_x.append(409)
        indici_x.append(417)
    return indici_x

def highact(tempo, photons_flux, label, folder, save_to_file):

    label = os.path.basename(label)

    folder = os.path.join(folder, 'High_activity') # Compongo la directory dove mettere la cartella

    # Creo la cartella dove mettero il png del plot e i dati
    if os.path.isdir(folder)==False:
        os.mkdir(folder)

    # uso la fuznione soglia() per ottenere la soglia adatta in base al file inviato

    theshold = soglia(label)

    photons_flux = np.asarray(photons_flux)

    # Maschera per filtare le quiescenze

    filtered_quiescence = photons_flux < theshold  

    # Faccio una copia dei dati

    high_activity_data = photons_flux.copy()

    # Applico la maschera per ottenre solo le alte attivita

    high_activity_data[filtered_quiescence] = 0.0  #Pongo a zero tutto cio sotto a theshold

    # Richiamo la funzine alta_attvita per farmi dare il numero di alte attivita e la loro durata
    # e l afunzione indice_x per poi graficare le linee delimitano uno stato di alta attivita

    n_high, len_high = alta_attivita(label)
    indici = line_high_activity(label)

    figure, ax = plt.subplots(figsize=(10, 7))
    plt.title('LAT Light Curve')
    plt.plot(tempo, photons_flux, 'o-', color='black' , label = label)
    plt.plot(tempo, np.full(len(tempo), theshold), color = 'red', label = 'Theshold : {:} [Gev]'.format(theshold))
    plt.legend()
    for i in indici:
        plt.axvline(tempo[i], color = 'blue')  # Delimito i vari stati alti
    #plt.yscale('log')
    plt.xlabel('Time [d]')
    plt.ylabel(r'Photon Flux ($ph$ $cm^{-2}$ $s^{-1}$)')
    if save_to_file:
        plt.savefig(os.path.join(folder, "Plot_high_activity.png"))
    else:
        plt.show()
    plt.close(figure)

    if save_to_file:
        d1 = {'Photon_Flux [Photon Flux [0.1-100 GeV](photons cm-2 s-1)]' : high_activity_data, 'Tempo[d]' : tempo}
        d2 = {'Stati alta attivita' : np.arange(1,len(len_high)+1, 1),  'Durata [d]': len_high}
        df1 = pd.DataFrame(data = d1)
        df2 = pd.DataFrame(data = d2)
        df1.to_csv(os.path.join(folder, 'Dati_only_high_activity.txt'), index = False)
        df2.to_csv(os.path.join(folder, 'Dati_numero_durata_high_activity.txt'), index = False)
    else:
        print('Il numero di stati di alta attivita è : {:d}'.format(n_high), ' e la loro durata è : ', *len_high, 'giorni')


