contenuto = "Questo è il primo file di testo creato da Sofia"
f = open("primo_file_di_testo.txt", "w")
f.write(contenuto)
f.close()

nuova_stringa = "Aggiungo una nuova riga di testo!"
f = open("primo_file_di_testo.txt", "a")
f.write(f"\n{nuova_stringa}")
f.close()

# creiamo un secondo file di testo
# mettiamo un po' di contenuto (righe) e poi leggiamole
# ci sono due metodi: leggo tutto il contenuto e ciclo tutte le righe

print("metodo 1 --> mette tutto il contenuto in una lista di stringhe")
f = open("secondo_file_di_testo.txt", "r")
contenuto = f.readlines()
print(contenuto)

print("metodo 2 --> vede il file di testo come una lista di stringhe e le cicla")
f = open("secondo_file_di_testo.txt", "r")
riga = f.readline()
while riga != "":
    print(riga)
    riga = f.readline()

f.close()

# Esercizio 1: Proviamo a scrivere tutte le schede studente

# Proviamo a stampare la stessa cosa con tkinter??

import os
os.getcwd()

# per copiare, spostare, cancellare rinominare file a Sofia può essere utile guardare questa guida :
# https://www.programmareinpython.it/gestire-file-cartelle-e-file-system-con-python/i-files-come-copiarli-spostarli-rinominarli-o-cancellarli/
# https://www.programmareinpython.it/gestire-file-cartelle-e-file-system-con-python/come-usare-le-cartelle-in-python/

# Vedere se sofia ha excel!!!

