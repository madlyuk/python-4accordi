

persone = [
            { 
                "tipo": "alunno",
                "nome":"Mario",
                "cognome":"Rossi",
                "età":12,
                "classe":2,
                "sezione":"A",
                "residenza":"via Cisa",
                "città": "Marmirolo"
            },
            { 
                "tipo": "alunno",
                "nome":"Francesco",
                "cognome":"Tosetti",
                "età":12,
                "classe":2,
                "sezione":"B",
                "residenza":"via Bertolotti",
                "città": "Mantova"
            },
            { 
                
                "tipo": "alunno",
                "nome":"Luca",
                "cognome":"Sgarbi",
                "età":13,
                "classe":2,
                "sezione":"A",
                "residenza":"via Marmore",
                "città": "Mantova"
            },
            { 
                "tipo": "alunno",
                "nome":"Sandro",
                "cognome":"Pedroni",
                "età":12,
                "classe":2,
                "sezione":"B",
                "residenza":"via Delle Torri 12",
                "città": "Borgovirgilio"
            },
            { 
                
                "tipo": "alunno",
                "nome":"Mauro",
                "cognome":"Dall'Olio",
                "età":12,
                "classe":1,
                "sezione":"B",
                "residenza":"via Cisa",
                "città": "Motteggiana"
            },
            { 
                
                "tipo": "alunno",
                "nome":"Franco",
                "cognome":"Stecca",
                "età":11,
                "classe":2,
                "sezione":"B",
                "residenza":"via Pompilio 2",
                "città": "Suzzara"
            },
            { 
                "tipo": "alunno",
                "nome":"Walter",
                "cognome":"Vicentini",
                "età":12,
                "classe":1,
                "sezione":"B",
                "residenza":"via Tassoni",
                "città": "Gonzaga"
            },
            {
                "tipo": "alunno",
                "nome":"Mario",
                "cognome":"Rossi",
                "età":11,
                "classe":1,
                "sezione":"A",
                "residenza":"via Gioia 21",
                "città": "Mantova"
            },
            {
                "tipo": "professore",
                "nome": "antonella",
                "cognome": "pinottii",
                "materie": ["italiano","storia","geografia"],
                "classe": [1,2,3],
                "sezione": ["a"],
            },
            {
                "tipo": "professore",
                "nome": "andrea",
                "cognome": "gozzoli",
                "materie": ["matematica","geometria"],
                "classe": [1,2,3],
                "sezione": ["a"],
            },
            {
                "tipo": "professore",
                "nome": "giulia",
                "cognome": "domenici",
                "materie": ["italiano","storia","geografia"],
                "classe": [1,2,3],
                "sezione": ["b"],
            },
            {
                "tipo": "professore",
                "nome": "antonella",
                "cognome": "pinottii",
                "materie": ["matematica","geometria"],
                "classe": [1,2,3],
                "sezione": ["b"],
            },
            {
                "tipo": "professore",
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
    

def stampa_schede(persone):
    for persona in persone:
        if persona.get("tipo") == "alunno":
            print(get_scheda_alunno(persona))
        else:
            print(get_scheda_prof(persona))

stampa_schede(persone)




