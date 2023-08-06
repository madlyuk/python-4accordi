from lezione6_class import Scuola, Persona, Studente, Insegnante
from lezione6_database import alunni, professori

def stampa_lista_schede(lista):
    for elemento in lista:
        print(elemento.scheda_personale())

def crea_tutti_gli_alunni(alunni):
    ret = []
    for alunno in alunni:
        studente = Studente(
            nome=alunno.get("nome"), 
            cognome=alunno.get("cognome"), 
            età=alunno.get("età"), 
            residenza=alunno.get("residenza"), 
            città=alunno.get("città"), 
            classe_attuale=alunno.get("classe_attuale"), 
            scuola=alunno.get("scuola")
        )
        ret.append(studente)
    return ret

def crea_tutti_i_professori(professori):
    ret = []
    for professore in professori:
        studente = Insegnante(
            nome=professore.get("nome"), 
            cognome=professore.get("cognome"), 
            età=professore.get("età"), 
            residenza=professore.get("residenza"), 
            città=professore.get("città"), 
            scuola=professore.get("scuola"),
            materie=professore.get("materie")
        )
        ret.append(studente)
    return ret

if __name__ == '__main__':
    lista_studenti = crea_tutti_gli_alunni(alunni)
    lista_professori = crea_tutti_i_professori(professori)
    
    print("""
          ---- STAMPIAMO TUTTI GLI STUDENTI ---- 
          
          """)

    stampa_lista_schede(lista_studenti)
    print("""
          ---- STAMPIAMO TUTTI I PROFESSORI ---- 

          """)
    stampa_lista_schede(lista_professori)
    