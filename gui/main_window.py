# Main Window for the PKU Control Application
# Simple Python Programm to control the Phenylketonuria (PKU) diet and to store Phenylalanine (Phe) and Tyrosin values in a SQLite database
# Author: Toni Dahlitz
# Date: 2025-02-21
# Version: 0.1

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
import backend.backend as backend

class main_gui:
    def __init__(self, root, callback):

        # Main Window
        self.root = root
        self.root.title("PKU Control")
        self.root.geometry("1200x600")
        self.callback = callback 

        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(6, weight=1) 

        # Widgets
        # Phe Value
        self.phevalue_label = tk.Label(self.root, text="Phe-Wert")
        self.phevalue_entry = tk.Entry(self.root)
        self.phevalue_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.phevalue_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Tyr Value
        self.tyrvalue_label = tk.Label(self.root, text="Tyr-Wert")
        self.tyrvalue_entry = tk.Entry(self.root)
        self.tyrvalue_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.tyrvalue_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Date
        self.date_label = tk.Label(self.root, text="Datum")
        self.date_entry = tk.Entry(self.root)
        self.date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Comment
        self.comment_label = tk.Label(self.root, text="Kommentar")
        self.comment_entry = tk.Entry(self.root)
        self.comment_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.comment_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Save
        self.save_button = tk.Button(self.root, text="Speichern", command=self.save_values)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Table
        self.tree = tk.ttk.Treeview(self.root, columns=("Datum", "Phe", "Tyr", "Kommentar"), show="headings")
        self.tree.grid(row=0, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        # Headings
        self.tree.heading("Datum", text="Datum")
        self.tree.heading("Phe", text="Phe-Wert")
        self.tree.heading("Tyr", text="Tyr-Wert")
        self.tree.heading("Kommentar", text="Kommentar")

        # Column width and alignment
        self.tree.column("Datum", width=100, anchor=tk.W)
        self.tree.column("Phe", width=80, anchor=tk.W)
        self.tree.column("Tyr", width=80, anchor=tk.W)
        self.tree.column("Kommentar", width=200, anchor=tk.W)

        # Load Button
        self.load_button = tk.Button(root, text="Daten laden", command=self.load_data)
        self.load_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        # Frame for the chart
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        

        #Laden der Daten
        self.load_data()
        self.show_chart()

    def show_chart(self):
        data = self.load_data()  # Load data from the database

        if not data:
            print("Keine Daten vorhanden!")
            return

        dates = [entry[0] for entry in data]  # Date (Column 3)
        phe_values = [float(entry[1]) for entry in data]  # Phe-Value (Column 1)

        # Sort the data by date
        dates, phe_values = zip(*sorted(zip(dates, phe_values)))

        # Matplotlib-Chart create
        fig, ax = plt.subplots(figsize=(4, 3))
        fig.patch.set_facecolor("gray")  # Hintergrund des gesamten Diagramms

        ax.plot(dates, phe_values, marker="o", linestyle="-", color="white", label="Phe-Wert")  # Liniendiagramm
        
        # Axis-Labels
        ax.set_xlabel("Datum", fontsize=5)
        ax.set_ylabel("Phe-Wert", fontsize=5)
        ax.set_title("Phe-Werte über die Zeit", fontsize=6)
        ax.tick_params(axis="x", labelsize=6)
        ax.tick_params(axis="y", labelsize=6)
        ax.set_facecolor("gray")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        ax.tick_params(axis="both", colors="white")

        # Paste the chart into the tkinter window
        for widget in self.canvas_frame.winfo_children():
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
        data = backend.database.show_data()

        if not data:
            print("Fehler: Keine Daten gefunden!")
            return

        # Delete all rows from the table
        for row in self.tree.get_children():
            self.tree.delete(row)

        for entry in data:
            self.tree.insert("", "end", values=entry)  # Insert tuple into the treeview
        return data

def mainloop(self):
    self.root.mainloop()
