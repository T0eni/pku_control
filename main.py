# Simple Python Programm to control the Phenylketonuria (PKU) diet and to store Phenylalanine (Phe) and Tyrosin values in a SQLite database
# Author: Toni Dahlitz
# Date: 2025-02-12
# Version: 0.1

import tkinter as tk
import backend
from gui.main_window import main_gui  # Importiere die GUI-Klasse

def on_values_saved(date, phe, tyr, comment):
    print(f"Datum: {date}")
    print(f"Phe-Wert: {phe}")
    print(f"Tyr-Wert: {tyr}")
    print(f"Kommentar: {comment}")
    
    """ Diese Funktion speichert die Werte in die Datenbank """
    backend.database.insert_data(phe, tyr, date, comment)  # Backend übernimmt die Logik    

if __name__ == "__main__":
    root = tk.Tk()  # Tkinter Hauptfenster erstellen
    app = main_gui(root, on_values_saved)  # GUI-Instanz erstellen
    root.mainloop()  # Tkinter Hauptloop starten