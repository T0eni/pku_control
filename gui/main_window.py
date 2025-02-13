# Main Window of the GUI
# Author: Toni Dahlitz
# Date: 2025-02-12
# Version: 0.1

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
import backend

class main_gui:
    def __init__(self, root, callback):

        #Tkinter-Fenster erstellen
        self.root = root   # Erstelle ein neues Tkinter-Fenster
        self.root.title("PKU Control")  # Fenster
        self.root.geometry("1200x600")  # Fenster-Größe
        self.callback = callback # Callback-Funktion

        self.root.grid_columnconfigure(2, weight=1)  # Spalte mit der Tabelle soll sich anpassen
        self.root.grid_rowconfigure(6, weight=1)    # Zeile mit der Tabelle soll sich anpassen

        # Inhalt
        # Label und Eingabefeld für den Phe-Wert
        self.phevalue_label = tk.Label(self.root, text="Phe-Wert")
        self.phevalue_entry = tk.Entry(self.root)
        self.phevalue_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.phevalue_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Label und Eingabefeld für den Tyr-Wert
        self.tyrvalue_label = tk.Label(self.root, text="Tyr-Wert")
        self.tyrvalue_entry = tk.Entry(self.root)
        self.tyrvalue_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.tyrvalue_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Label und Eingabefeld für das Datum
        self.date_label = tk.Label(self.root, text="Datum")
        self.date_entry = tk.Entry(self.root)
        self.date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Label und Eingabefeld für den Kommentar
        self.comment_label = tk.Label(self.root, text="Kommentar")
        self.comment_entry = tk.Entry(self.root)
        self.comment_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.comment_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Button zum Speichern der Werte
        self.save_button = tk.Button(self.root, text="Speichern", command=self.save_values)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.tree = tk.ttk.Treeview(self.root, columns=("Datum", "Phe", "Tyr", "Kommentar"), show="headings")
        self.tree.grid(row=0, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        # Spaltenüberschriften setzen
        self.tree.heading("Datum", text="Datum")
        self.tree.heading("Phe", text="Phe-Wert")
        self.tree.heading("Tyr", text="Tyr-Wert")
        self.tree.heading("Kommentar", text="Kommentar")

        # Spaltenbreiten anpassen
        self.tree.column("Datum", width=100, anchor=tk.W)
        self.tree.column("Phe", width=80, anchor=tk.W)
        self.tree.column("Tyr", width=80, anchor=tk.W)
        self.tree.column("Kommentar", width=200, anchor=tk.W)

        # Button, um die Tabelle zu aktualisieren
        self.load_button = tk.Button(root, text="Daten laden", command=self.load_data)
        self.load_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        # Frame für das Diagramm
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        

        #Laden der Daten
        self.load_data()
        self.show_chart()

    def show_chart(self):
        """Lädt die Daten aus der DB und zeigt sie als Liniendiagramm an."""
        data = self.load_data()  # Daten aus der DB abrufen

        if not data:  # Falls keine Daten vorhanden sind
            print("Keine Daten vorhanden!")
            return

        dates = [entry[0] for entry in data]  # Datum (Spalte 3)
        phe_values = [float(entry[1]) for entry in data]  # Phe-Werte (Spalte 1)

        # Matplotlib-Figur erstellen
        fig, ax = plt.subplots(figsize=(4, 3))
        fig.patch.set_facecolor("gray")  # Hintergrund des gesamten Diagramms

        ax.plot(dates, phe_values, marker="o", linestyle="-", color="white", label="Phe-Wert")  # Liniendiagramm

        # Achsenbeschriftungen & Titel
        ax.set_xlabel("Datum", fontsize=5)
        ax.set_ylabel("Phe-Wert", fontsize=5)
        ax.set_title("Phe-Werte über die Zeit", fontsize=6)
        #ax.legend()  # Legende hinzufügen
        #ax.grid(True)  # Gitternetz aktivieren
        ax.tick_params(axis="x", labelsize=6)  # X-Achsenskalierung
        ax.tick_params(axis="y", labelsize=6)  # Y-Achsenskalierung
        ax.set_facecolor("gray")  # Hintergrund des Diagrammbereichs
        ax.xaxis.label.set_color("white")  # X-Achsen-Beschriftung
        ax.yaxis.label.set_color("white")  # Y-Achsen-Beschriftung
        ax.title.set_color("white")  # Titel
        ax.tick_params(axis="both", colors="white")  # Achsenwerte in Weiß


        # Diagramm in Tkinter-Fenster einfügen
        for widget in self.canvas_frame.winfo_children():  # Altes Diagramm entfernen
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def save_values(self):
        """ Speichert die Werte und übergibt sie an main.py """
        phe_value = self.phevalue_entry.get()
        tyr_value = self.tyrvalue_entry.get()
        date_value = self.date_entry.get()
        comment_value = self.comment_entry.get()

        self.callback(phe_value, tyr_value, date_value, comment_value)
        self.load_data()

    def load_data(self):
        data = backend.database.show_data()  # Holt Daten aus backend.py

        if not data:  # Falls `None` oder leere Liste zurückkommt
            print("Fehler: Keine Daten gefunden!")
            return

        # Vorherige Einträge in der Tabelle löschen, um doppelte Einträge zu vermeiden
        for row in self.tree.get_children():
            self.tree.delete(row)

        """Holt die Daten aus der DB und fügt sie in die Tabelle ein"""
        for entry in data:
            self.tree.insert("", "end", values=entry)  # Tupel direkt einfügen
        return data


# Tkinter-Loop starten
def mainloop(self):
    self.root.mainloop()
