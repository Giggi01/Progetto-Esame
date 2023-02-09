import sys
import os

import read as r
import plot as plt
import fourier as ft
import noise as n
import filtro as fl
import highactivity as h

files = []
save_to_file = False


# def make_functions(path):
def make_functions():
    global files
    attributes = []
    for file in files:
        print(f'FILE: {file}')
        # tempo, photons_flux, photon_error = r.read(path)
        attributes.append([file, os.path.basename(file), r.read(file, save_to_file)])
    for attribute in attributes:
        # grafico = plt.plot(tempo, photons_flux, photon_error,
        #                 os.path.basename(path))
        plt.plot(attribute[2][0], attribute[2][1], attribute[2][2],
                 attribute[1], attribute[0], save_to_file)
    for attribute in attributes:
        # fft, freq, pot = ft.fourier(photons_flux, tempo, os.path.basename(path))
        attribute[2] += ft.fourier(attribute[2][1], attribute[2][0], attribute[1], attribute[0], save_to_file)
    for attribute in attributes:
        # params, params_cov = n.noise(freq, pot, os.path.basename(path))
        n.noise(attribute[2][4], attribute[2][5], attribute[1],
                attribute[0], save_to_file)
    for attribute in attributes:
        # filtered_LC05, filtered_LC02, filtered_LC01 = fl.filter(
        #     freq, fft, tempo, photons_flux, os.path.basename(path))
        fl.filter(
            attribute[2][4], attribute[2][3], attribute[2][0], attribute[2][1], attribute[1], attribute[0], save_to_file)
    for attribute in attributes:
        if (attribute[0])[len(attribute[0])-10:len(attribute[0])] == 'weekly.csv':  # uso solo il campionamento daily per tovare periodo di alta attivita
            h.highact(attribute[2][0], attribute[2][1], os.path.dirname(attribute[0]), os.path.dirname(attribute[0]), save_to_file)



def recursive_call(path):
    global files
    if os.path.isfile(path):
        if os.path.splitext(path)[1] == '.csv':
            files.append(path)
            # make_functions(path)
    elif os.path.isdir(path):
        for element in os.listdir(path):
            recursive_call(os.path.join(path, element))
    else:
        print(f'{path} is not a valid path')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Errore. Inserire percorso del file o della directory')
    else:
        if '--file' in sys.argv[1:]:
            save_to_file = True
        for path in sys.argv[1:]:
                if path!= '--file':
                    recursive_call(path)
        # Controllare che file sia > 0
        make_functions()
