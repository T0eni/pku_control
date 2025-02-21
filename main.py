# Simple Python Programm to control the Phenylketonuria (PKU) diet and to store Phenylalanine (Phe) and Tyrosin values in a SQLite database
# Author: Toni Dahlitz
# Date: 2025-02-21
# Version: 0.1

import tkinter as tk
import backend.backend as backend
from gui.main_window import main_gui

def on_values_saved(date, phe, tyr, comment):
    print(f"Datum: {date}")
    print(f"Phe-Wert: {phe}")
    print(f"Tyr-Wert: {tyr}")
    print(f"Kommentar: {comment}")
    
    backend.database.insert_data(phe, tyr, date, comment)    

if __name__ == "__main__":
    root = tk.Tk()
    app = main_gui(root, on_values_saved)
    root.mainloop()