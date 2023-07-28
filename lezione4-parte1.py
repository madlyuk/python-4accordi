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


def get_scheda_alunno(alunno):
    scheda = f"""
            Alunno: {alunno.get("nome")} {alunno.get("cognome")}
            ------------------------
            età: {alunno.get("età")}
            classe/sezione: {alunno.get("classe")}{alunno.get("sezione")}
            Abita in: {alunno.get("residenza")} -  {alunno.get("città")}
            ------------------------
        """
    return scheda

def get_scheda_prof(prof):
    scheda = f"""
            Professore: {prof.get("nome")} {prof.get("cognome")}
            ------------------------
            materie: {prof.get("materie")}
            classi: {prof.get("classe")}
            sezioni: {prof.get("sezioni")} 
            ------------------------
        """
    return scheda
    
def stampa_schede_alunni(alunni):
    for alunno in alunni:
        print(get_scheda_alunno(alunno))

def stampa_schede_prof(professori):
    for prof in professori:
        print(get_scheda_prof(prof))

stampa_schede_alunni(alunni)
stampa_schede_prof(professori)





