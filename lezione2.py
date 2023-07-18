print(" --- Esempio 1: vediamo i tipi di variabili ---")

var1= "Questa è una stringa"
var2= 1
var3= 3.14
var4= [0,1,2,3,4,5,6,7,8,9]
var4= { 
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


print(" --- Esempio 3: convertiamo i tipi delle variabili --- ")

name = "Mario"
age = 30
# Questo è un commento:
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

print(" --- Esempio 4 --- ")


