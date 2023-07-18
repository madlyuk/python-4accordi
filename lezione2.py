# Questo è un commento, basta mettere all'inizio della riga il simbolo cancelletto
"""
Anche questo è un commento,
ma questa volta è fatto su più righe.
Gli IDE in generale permettono di selezionare più righe e commentarle, 
ma lo fanno nel primo modo, inserendo i simboli "#"
"""
# Selezionare le righe che vogliamo commentare e premere: CTRL + k + c 
# Stessa cosa di prima, ma premendo CTRL + k + u per eliminare i commenti
# I commenti sono utili per rendere leggibile il codice a tutti e anche a noi stessi se passa troppo tempo

print(" --- Esempio 1: vediamo i tipi di variabili ---")

var1= "Questa è una stringa"
var2= 1
var3= 3.14
# i prossimi due tipi di varabili li vedremo più avanti
var4= [0,1,2,3,4,5,6,7,8,9]
var5 = True
var6= { 
        "nome":"Mario",
        "cognome":"Rossi",
        "età":48,
        "città":"Mantova",
        }

print(
    f"""
    var1={var1} - è una variabile di tipo {type(var1)};
    var2={var2} - è una variabile di tipo {type(var2)};
    var3={var3} - è una variabile di tipo {type(var3)};
    var4={var4} - è una variabile di tipo {type(var4)};
    var5={var5} - è una variabile di tipo {type(var5)};
    var6={var6} - è una variabile di tipo {type(var6)};
    
    """
)


print(" --- Esempio 2: come inserire contenuti tra apici dentro una stringa? --- ")
print(
    """
    e Dante scrisse: \"Nel mezzo del cammin di nostra vita...\"
    ...oppure...
    e Dante scrisse: 'Nel mezzo del cammin di nostra vita...'

    """
)

print(" --- Esempio 3: alcune funzioni delle stringhe --- ")
# abbiamo già visto la funzione capitalize() che imposta la prima lettera di una stringa in maiuscolo.
# Vediamo ora qualche altra funzione utile:
# replace() – sostituisce una substringa con un’altra
# startswith() – verifica se la stringa inizia con una particolare sequenza di caratteri
# endswith() – verifica se la stringa finisce con una particolare sequenza di caratteri
# upper() – converte tutti i caratteri della stringa in maiuscolo
# lower() – converte tutti i caratteri della stringa in minuscolo 

frase = "Il mio frutto preferito è il FICO d'INDIA.."
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.startswith("il"))
print(frase.lower().startswith("il"))
print(frase.endswith("india"))
print(frase.replace(".",""))
print(frase.lower().replace(".","").endswith("india"))

# Prendendo l'ultimo esempio avremmo anche potuto elaborare la frase e poi controllare se terminava con "india"
frase = frase.lower()
frase = frase.replace(".","")
print(frase.endswith("india"))

print(" --- Esempio 4: convertiamo i tipi delle variabili --- ")

name = "Mario"
age = 30
# se provassi a scrivere un testo concatenando le due variabili otterrei un errore:
# devo eseguire un "cast" della variabile numerica per convertirla in testo
print(f"L'utente {name} ha {age} anni!")
# in questo caso ho docuto convertire l'intero in quanto è all'interno della stringa
# Potrei pero' stampare solo la variabile age, e in questo caso python riconoscerebbe che deve fare la conversione in automatico:
print("L'utente " + name + " ha ")
print(age)
print(" anni!")
# Anche nelle operazioni numeriche devo fare la stessa conversione (al contrario però).. supponiamo di salvare due variabili numeriche come testo:
numero1="30"
numero2="4"
moltiplicazione = int(numero1) * int(numero2)
print(f"{numero1} x {numero2} = {str(moltiplicazione)}")

print(" --- Esempio 5: Alcune funzioni numeriche --- ")
# Alcune funzioni utili con i numeri
# Come per le stringhe,anche le variabili di tipo numerico hanno loro funzioni utili. 
# Di seguito ne riporto solo qualcuna di esempio:
# min() – questa funzione restituisce il valore minimo all’interno di una sequenza o una lista di numeri
# max() – questa funzione restituisce il valore massimo all’interno di una sequenza o una lista di numeri
# abs() – calcola il valore assoluto di un numero
# round() – questa funzione arrotonda il numero per un certo numero di cifre decimali
# sum() – calcola la somma di una lista di numeri

n1 = min(1,5,0,3,4,6)
print(n1)
n2 = max([1,5,0,3,4,6])
print(n2)
n3 = abs(-12)
print(n3)
n4 = round(3.145,1)
print(n4)
n5 = sum([1.3,5.2,-0.6,3.1,4.4,6.9])
print(n5) 

print(" --- Esempio 6: Operatori booleani --- ")

# OPERATORI DI COMPARAZIONE

# uguaglianza
risultato =  5 == 5
print("1: ", risultato)

risultato = not 5 == 6
print("2: ", risultato)

risultato = "io" == "robot"
print("3: ", risultato)

risultato = 33 == "33"
print("4: ", risultato)

risultato = str(33) == "33"
print("5: ", risultato)

# disuguaglianza
risultato = "prima" != "dopo"
print("6: ", risultato)

# maggiore, minore, maggiore uguale, minore uguale
risultato = 7 < 33
print("7: ", risultato)

risultato = 33 > 33
print("8: ", risultato)

risultato = 33 >= 33
print("9: ", risultato)



# OPERATORI DI COMPARAZIONE

# NOT
risultato = not True
print("10: ", risultato)

# OR
risultato = True or True
print("11: ", risultato)
risultato = True or False
print("12: ", risultato)
risultato = False or True
print("13: ", risultato)
risultato = False or False
print("14: ", risultato)

# AND
risultato = True and True
print("15: ", risultato)
risultato = True and False
print("16: ", risultato)
risultato = False and True
print("17: ", risultato)
risultato = False and False
print("18: ", risultato)


# Esempio più complesso
a = True
b = False
risultato = (a and not b) or (not a and b)
print("19: ", risultato)
