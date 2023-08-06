class Scuola:

    def __init__(self, nome, indirizzo, tipo_studi):
        self.nome = nome
        self.indirizzo = indirizzo
        self.tipo_studi = tipo_studi

    def scheda_personale(self):
        scheda = f"""
        Scuola: {self.nome}
        Indirizzo: {self.cognome}
        Tipo di studi: {self.età}\n"""
        return scheda

class Persona:

    def __init__(self, nome, cognome, età, residenza, città):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
        self.città = città

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}
        Città: {self.città}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza
        4 - Città""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")
        elif scelta == "5":
            self.città = input("Nuova Città --> ")


class Studente(Persona):
    profilo = "Studente"

    def __init__(self,nome, cognome, età, residenza, città, classe_attuale, scuola):
        super().__init__(nome, cognome, età, residenza, città)
        self.classe_attuale = classe_attuale
        self.scuola = scuola

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        ---------------------------
        Scuola: {self.scuola} 
        Classe attuale: {self.classe_attuale} 
        ***"""
        return super().scheda_personale() + scheda

    def cambio_classe(self,classe_attuale):
        self.classe_attuale = classe_attuale
        print(f"Classe Aggiornato")

    def cambio_scuola(self,scuola):
        self.scuola = scuola
        print(f"Scuola Aggiornata")


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self,nome, cognome, età, residenza, città, scuola, materie=None):
        super().__init__(nome, cognome, età, residenza, città)
        self.scuola = scuola
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Scuola:{self.scuola}
        Materie Insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda

    def aggiungi_materia(self,nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco Aggiornato")

    def cambio_scuola(self,scuola):
        self.scuola = scuola
        print(f"Scuola Aggiornata")