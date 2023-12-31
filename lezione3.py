# print("------------ ESEMPIO 1 --------------")
# # creo una stuttura per ctegorizzare gli alunni di una scuola 

# alunno = { 
#         "nome":"Mario",
#         "cognome":"Rossi",
#         "età":12,
#         "classe":2,
#         "sezione":"A",
#         "residenza":"via Delle Torri 12",
#         "città": "Mantova"
#         }

# scheda_alunno = f"""
#     Alunno: {alunno.get("nome")} {alunno.get("cognome")}
#     ------------------------
#     età: {alunno.get("età")}
#     classe/sezione: {alunno.get("classe")}{alunno.get("sezione")}
#     Abita in: {alunno.get("residenza")} -  {alunno.get("città")}
#     ------------------------
# """

# print(scheda_alunno)


# print("------------ ESEMPIO 2 --------------")
# alunno = {}
# print("Ora ti chiedo di inserire qualche dato dell'alunno: ")
# # GUARDARE LA CONVERSIONE DI TIPO E COME MODELLO LE STRINGHE!

# # SET dei valori nel dizionario
# alunno["nome"] = input("inserisci il nome: ").capitalize()
# alunno["cognome"] = input("inserisci il cognome: ").capitalize()
# alunno["età"] = int(input("inserisci l'età: "))
# alunno["classe"] = int(input("inserisci la classe: "))
# alunno["sezione"] = input("inserisci la sezione: ").upper()
# alunno["residenza"] = input("inserisci la sua residenza: ")
# alunno["città"] = input("inserisci la sua città: ").capitalize()

# # GET dei valori del dizionario
# scheda_alunno = f"""
#     Alunno: {alunno.get("nome")} {alunno.get("cognome")}
#     ------------------------
#     età: {alunno.get("età")}
#     classe/sezione: {alunno.get("classe")}{alunno.get("sezione")}
#     Abita in: {alunno.get("residenza")} -  {alunno.get("città")}
#     ------------------------
# """

# print(scheda_alunno)

# alunno["animale"] = input("Qual'è il tuo animale preferito? : ")

# scheda_alunno = scheda_alunno + f"""
#     Animale preferito: {alunno.get("animale")} 
#     ------------------------
# """
# print(scheda_alunno)

print("------------ ESEMPIO 3 --------------")
alunni = [] # --> ora ne inseriamo più di uno con un ciclo WHILE!
esci = False

print("Ora ti chiedo di inserire qualche dato dell'alunno: ")
# GUARDARE LA CONVERSIONE DI TIPO E COME MODELLO LE STRINGHE!

while not esci:
    # SET dei valori nel dizionario
    alunno = {}
    alunno["nome"] = input("inserisci il nome: ").capitalize()
    alunno["cognome"] = input("inserisci il cognome: ").capitalize()
    alunno["età"] = int(input("inserisci l'età: "))
    alunno["classe"] = int(input("inserisci la classe: "))
    alunno["sezione"] = input("inserisci la sezione: ").upper()
    end = input("Vuoi inserire un altro alunno? Scrivi 's' per SI o 'n' per NO: ").upper()
    
    # Aggiungo l'alunno alla mia lista di alunni
    alunni.append(alunno)
    
    if end == "N": # mi semplifico la vita mettendo in maiuscolo per non fare due controlli
        esci = True


professori = []
professore = {
        "nome": "mario rossi",
        "classe_sezione": "3A"
    }
professori.append(professore)

nuovo_professore={}
nuovo_professore["nome"] = "stefano bianchi"
nuovo_professore["classe"]="2B"
professori.append(nuovo_professore)

for alunno in alunni:
    
    # aggiungo l'informazione se c'è una bocciatura!
    classe = alunno.get("classe")
    anni = alunno.get("età")
    classe_sezione = str(alunno.get("classe")) + alunno.get("sezione") 

    # controllo se l'età super quella prevista dalla classe
    if (classe == 1) and anni > 11:
        bocciatura = True
    elif (classe == 2) and anni > 12:
        bocciatura = True
    elif (classe == 3) and anni > 13:
        bocciatura = True
    else:
        bocciatura = False
    
    scheda_alunno = f"""
        ----- {alunno.get("nome")} {alunno.get("cognome")} ----
        età: {anni}
        classe/sezione: {classe}{alunno.get("sezione")}
        bocciata/o: {bocciatura}

    """
    print(scheda_alunno)




