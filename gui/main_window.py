# Main Window of the GUI
# Author: Toni Dahlitz
# Date: 2025-02-07
# Version: 0.1

from tkinter import *

# Tkinter-Fenster erstellen
gui = Tk() # Erstelle ein neues Tkinter-Fenster
gui.title("PKU Control")   # Fenster-Titel
gui.geometry("800x400")     # Fenster-Größe
gui.configure(bg='#2b2b2b')  # Hintergrundfarbe

# Inhalt

# Label und Eingabefeld für den Phe-Wert
phevalue_label = Label(gui, text="Phe-Wert")
phevalue_entry = Entry(gui)
phevalue_label.pack(side = "top", anchor=W, padx=10, pady=10)
phevalue_entry.pack(side = "top", anchor=W, padx=10, pady=10)

# Label und Eingabefeld für den Tyr-Wert
#tyrvalue_label = Label(gui, text="Tyr-Wert")
#tyrvalue_entry = Entry(gui)

# Label und Eingabefeld für das Datum und den Kommentar
#date_label = Label(gui, text="Datum")
#comment_label = Label(gui, text="Kommentar")



#tyrvalue_label.pack()
#date_label.pack()
#comment_label.pack()


# Tkinter-Loop starten
gui.mainloop()