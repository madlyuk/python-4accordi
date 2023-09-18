# Link utili: https://www.programmareinpython.it/interfacce-grafiche-python-con-tkinter/1-introduzione-alle-gui-con-tkinter/
# richiede sudo apt-get install python3-tk

# tiferimenti: https://www.pythontutorial.net/tkinter/tkinter-listbox/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from lezione6_class import Studente
from lezione6_database import alunni

# se dobbiamo fare chiamate ad API
# import requests

window = tk.Tk()

window.geometry("600x600")
window.title("Hello TkInter!")
window.resizable(False, False)
window.configure(background="white")



def search_student(id):
    ret = False
    for alunno in alunni:

        if int(id) == int(alunno.get("id")):
            ret = Studente(
                nome=alunno.get("nome"),
                cognome=alunno.get("cognome"),
                età=alunno.get("età"),
                residenza=alunno.get("residenza"),
                città=alunno.get("città"),
                classe_attuale=alunno.get("classe_attuale"),
                scuola=alunno.get("scuola")
            )
    return ret



def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    print(selected_indices)
    # get selected items
    # selected_student = ",".join([listbox.get(i) for i in
    #                              selected_indices])
    selected_student = search_student(selected_indices[0])
    msg = f'You selected: {selected_student.scheda_personale()}'
    # visualizzo la selezione in un alert
    showinfo(title='Information', message=msg)


# ---- List box ----

# langs = ('Java', 'C#', 'C', 'C++', 'Python',
#          'Go', 'JavaScript', 'PHP', 'Swift')

# var = tk.Variable(value=langs)

# lista_studenti = crea_tutti_gli_alunni(alunni)
# var = tk.Variable(value=lista_studenti)


frame = ttk.Frame()
# Create a scrollbar with vertical orientation.
# scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)



listbox = tk.Listbox(
    # frame,
    window,
    # listvariable=var,
    # height=3,
    # selectmode=tk.SINGLE,
    # yscrollcommand=scrollbar.set
)

for alunno in alunni:
    # listbox.insert(tk.END, alunno.get("nome") + " " + alunno.get("cognome"))
    listbox.insert(alunno.get("id"), alunno.get("nome") + " " + alunno.get(
        "cognome"))


# scrollbar.config(command=listbox.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# listbox.pack(expand=True, fill=tk.BOTH)
listbox.pack()
# frame.pack()

listbox.bind('<<ListboxSelect>>', items_selected)



# ---- Fine list box ----

if __name__ == "__main__":
    window.mainloop()
