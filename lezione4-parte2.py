

alunni = [
            { 
                "nome":"Mario",
                "cognome":"Rossi",
                "età":12,
                "classe":2,
                "sezione":"A",
                "residenza":"via Cisa",
                "città": "Marmirolo"
            },
            { 
                "nome":"Francesco",
                "cognome":"Tosetti",
                "età":12,
                "classe":2,
                "sezione":"B",
                "residenza":"via Bertolotti",
                "città": "Mantova"
            },
            { 
                "nome":"Luca",
                "cognome":"Sgarbi",
                "età":13,
                "classe":2,
                "sezione":"A",
                "residenza":"via Marmore",
                "città": "Mantova"
            },
            { 
                "nome":"Sandro",
                "cognome":"Pedroni",
                "età":12,
                "classe":2,
                "sezione":"B",
                "residenza":"via Delle Torri 12",
                "città": "Borgovirgilio"
            },
            { 
                "nome":"Mauro",
                "cognome":"Dall'Olio",
                "età":12,
                "classe":1,
                "sezione":"B",
                "residenza":"via Cisa",
                "città": "Motteggiana"
            },
            { 
                "nome":"Franco",
                "cognome":"Stecca",
                "età":11,
                "classe":2,
                "sezione":"B",
                "residenza":"via Pompilio 2",
                "città": "Suzzara"
            },
            { 
                "nome":"Walter",
                "cognome":"Vicentini",
                "età":12,
                "classe":1,
                "sezione":"B",
                "residenza":"via Tassoni",
                "città": "Gonzaga"
            },
            { 
                "nome":"Mario",
                "cognome":"Rossi",
                "età":11,
                "classe":1,
                "sezione":"A",
                "residenza":"via Gioia 21",
                "città": "Mantova"
            },
        ]

professori = [
                {
                    "nome": "antonella",
                    "cognome": "pinottii",
                    "materie": ["italiano","storia","geografia"],
                    "classe": [1,2,3],
                    "sezione": ["a"],
                },
                {
                    "nome": "andrea",
                    "cognome": "gozzoli",
                    "materie": ["matematica","geometria"],
                    "classe": [1,2,3],
                    "sezione": ["a"],
                },
                {
                    "nome": "giulia",
                    "cognome": "domenici",
                    "materie": ["italiano","storia","geografia"],
                    "classe": [1,2,3],
                    "sezione": ["b"],
                },
                {
                    "nome": "antonella",
                    "cognome": "pinottii",
                    "materie": ["matematica","geometria"],
                    "classe": [1,2,3],
                    "sezione": ["b"],
                },
                {
                    "nome": "federica",
                    "cognome": "lanzoni",
                    "materie": ["disegno"],
                    "classe": [1,2,3],
                    "sezione": ["b","a"],
                }
            ]


def get_alunni_per_classe(classe=None):
    ret = []
    for alunno in alunni:
        if classe and alunno["classe"] == classe:
            ret.append(alunno)
    return ret

def get_alunni_per_sezione(sezione=None):
    # Metodo 1:
    ret = []
    for alunno in alunni:
        if sezione and str(alunno["sezione"]).upper() == sezione.upper():
            ret.append(alunno)
    return ret

def get_alunni_per_classe_e_sezione(classe,sezione):
    ret = []
    alunni_nella_classe = get_alunni_per_classe(classe)
    alunni_nella_sezione = get_alunni_per_sezione(sezione)
    # se fosse così semplice, ma non lo è!!!
    # a = ["a","b","c"]
    # b = ["a","f","c"]
    # print( set(a).intersection(b) )
    for alunno in alunni_nella_classe:
        if alunno in alunni_nella_sezione:
            ret.append(alunno)
    return ret
    

# for alunno in alunni:

#     scheda_alunno = f"""
#         ----- {alunno.get("nome")} {alunno.get("cognome")} ----
#         età: {anni}
#         classe/sezione: {classe}{alunno.get("sezione")}

#     """
#     print(scheda_alunno)

# print( get_alunni_per_classe(1))

# print( get_alunni_per_sezione("a"))



print( get_alunni_per_classe_e_sezione(1,"a"))




