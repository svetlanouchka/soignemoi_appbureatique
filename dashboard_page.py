import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
import config  

import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
import config

class DashboardPage(tk.Frame):
    def __init__(self, parent, show_patient_details_callback):
        super().__init__(parent)
        self.parent = parent
        self.show_patient_details = show_patient_details_callback
        
        # Initialisation des attributs
        self.entries = {}
        self.sorties = {}

        # Création des widgets
        self.create_widgets()

        # Chargement des données
        self.load_entries()
        self.load_sorties()

    def create_widgets(self):
        # Création des widgets pour la page dashboard

        # Section Entrées
        tk.Label(self, text="Entrées").pack()
        self.entries_listbox = tk.Listbox(self)
        self.entries_listbox.pack()
        self.entries_listbox.bind("<<ListboxSelect>>", self.on_entry_select)

        # Section Sorties
        tk.Label(self, text="Sorties").pack()
        self.sorties_listbox = tk.Listbox(self)
        self.sorties_listbox.pack()
        self.sorties_listbox.bind("<Double-1>", self.on_sortie_select)

    def load_entries(self):
        try:
            response = requests.get(config.ENTRIES_URL)
            response.raise_for_status()
            entries_data = response.json()
            self.entries = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in entries_data}
            self.update_listbox_entries()  # Mise à jour de la Listbox des entrées
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API pour les entrées: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des entrées")

    def load_sorties(self):
        try:
            response = requests.get(config.SORTIES_URL)
            response.raise_for_status()
            sorties_data = response.json()
            self.sorties = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in sorties_data}
            self.update_listbox_sorties()  # Mise à jour de la Listbox des sorties
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API pour les sorties: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des sorties")

    def update_listbox_entries(self):
        self.entries_listbox.delete(0, tk.END)
        for patient_name in self.entries.keys():
            self.entries_listbox.insert(tk.END, patient_name)

    def update_listbox_sorties(self):
        self.sorties_listbox.delete(0, tk.END)
        for patient_name in self.sorties.keys():
            self.sorties_listbox.insert(tk.END, patient_name)

    def on_entry_select(self, event):
        selection = self.entries_listbox.curselection()
        if selection:
            patient_name = self.entries_listbox.get(selection[0])
            patient_id = self.entries.get(patient_name)
            if patient_id:
                self.show_patient_details(patient_id)
            else:
                messagebox.showerror("Erreur", "ID du patient non trouvé.")

    def on_sortie_select(self, event):
        selection = self.sorties_listbox.curselection()
        if selection:
            patient_name = self.sorties_listbox.get(selection[0])
            patient_id = self.sorties.get(patient_name)
            if patient_id:
                self.show_patient_details(patient_id)
            else:
                messagebox.showerror("Erreur", "ID du patient non trouvé.")

'''
class DashboardPage(tk.Frame):
    def __init__(self, parent, show_patient_details_callback):
        super().__init__(parent)
        self.parent = parent
        self.show_patient_details = show_patient_details_callback
        
        # Initialisation de l'attribut entries
        self.entries = {}
        
        self.create_widgets()
        self.load_entries()

    def create_widgets(self):
        # Création des widgets pour la page dashboard
        self.listbox_entries = tk.Listbox(self)
        self.listbox_entries.pack()
        self.listbox_entries.bind('<<ListboxSelect>>', self.on_entry_select)
        tk.Label(self, text="Entrées").pack()
        self.entries_listbox = tk.Listbox(self)
        self.entries_listbox.pack()
        self.entries_listbox.bind("<<ListboxSelect>>", self.on_entry_select)

        # Sorties Section
        tk.Label(self, text="Sorties").pack()
        self.sorties_listbox = tk.Listbox(self)
        self.sorties_listbox.pack()
        self.sorties_listbox.bind("<Double-1>", self.on_sortie_select)

    def load_entries(self):
        try:
            response = requests.get(config.ENTRIES_URL)
            response.raise_for_status()
            entries_data = response.json()
            self.entries = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in entries_data}
            self.update_listbox()  # Appel à update_listbox
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des données")

    def load_sorties(self):
        try:
            response = requests.get(config.SORTIES_URL)
            response.raise_for_status()
            sorties_data = response.json()
            self.sorties = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in sorties_data}
            self.update_listbox()  # Appel à update_listbox
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des données")

    def update_listbox(self):
        self.listbox_entries.delete(0, tk.END)
        for patient_name in self.entries.keys():
            self.listbox_entries.insert(tk.END, patient_name)

    def on_entry_select(self, event):
        selected_index = self.listbox_entries.curselection()
        if selected_index:
            patient_name = self.listbox_entries.get(selected_index)
            patient_id = self.entries.get(patient_name)  # Utilisez get pour éviter KeyError
            if patient_id:
                self.show_patient_details(patient_id)
            else:
                messagebox.showerror("Erreur", "ID du patient non trouvé.")

"""
class DashboardPage(tk.Frame):
    def __init__(self, parent, show_patient_details):
        super().__init__(parent)
        self.parent = parent
        self.show_patient_details = show_patient_details
        self.create_widgets()
        self.entries = {}
        self.load_entries()
        self.load_sorties()

    def create_widgets(self):
        tk.Label(self, text="Dashboard").pack(pady=10)

        # Entrées Section
        tk.Label(self, text="Entrées").pack()
        self.entries_listbox = tk.Listbox(self)
        self.entries_listbox.pack()
        self.entries_listbox.bind("<<ListboxSelect>>", self.on_entry_select)

        # Sorties Section
        tk.Label(self, text="Sorties").pack()
        self.sorties_listbox = tk.Listbox(self)
        self.sorties_listbox.pack()
        self.sorties_listbox.bind("<Double-1>", self.on_sortie_select)
'''
'''
    def load_entries(self):
        try:
            response = requests.get(config.ENTRIES_URL)
            response.raise_for_status()
            entries_data = response.json()
            self.entries = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in entries_data}
            self.update_listbox()
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des données")

    def load_sorties(self):
        try:
            response = requests.get(config.SORTIES_URL)
            response.raise_for_status()
            sorties_data = response.json()
            self.sorties = {f"{entry['prenom']} {entry['nom']}": entry['user_id'] for entry in sorties_data}
            self.update_listbox()
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des données")
    
    def update_listbox(self):
        self.listbox_entries.delete(0, tk.END)
        for patient_name in self.entries.keys():
            self.listbox_entries.insert(tk.END, patient_name)

    def on_entry_select(self, event):
        selection = self.entries_listbox.curselection()
        if selection:
            patient_id = self.entries_listbox.get(selection[0])
            print(f"Selected Patient ID: {patient_id}")
            self.show_patient_details(patient_id)

    def on_sortie_select(self, event):
        selection = self.sorties_listbox.curselection()
        if selection:
            patient_id = self.sorties_listbox.get(selection[0])
            self.show_patient_details(patient_id)
'''

