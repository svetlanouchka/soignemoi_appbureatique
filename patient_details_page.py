import tkinter as tk
from tkinter import messagebox
import requests
import config  

class PatientDetailsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        print("Creating patient details widgets...")
        tk.Label(self, text="Dossier du patient").pack(pady=10)
        # Augmentez la hauteur et la largeur du widget Text pour afficher plus de texte
        self.details_text = tk.Text(self, height=20, width=80)  # Ajustez ces valeurs selon vos besoins
        self.details_text.pack(expand=True, fill=tk.BOTH)

    def set_patient_id(self, patient_id):
        self.load_patient_details(patient_id)
    
    def load_patient_details(self, patient_id):
        try:
            response = requests.get(config.INFO_PATIENT_URL, params={'user_id': patient_id})
            response.raise_for_status()
            data = response.json()
        
            # Assumer que la clé dans data est le nom complet du patient
            patient_name = next(iter(data))  # Récupère la première clé du dictionnaire
            patient_info = data[patient_name]  # Accède aux détails du patient
        
            print("Patient Info:", patient_info)  # Debugging line
        
            # Assurez-vous que les clés existent et utilisez des valeurs par défaut si elles sont manquantes
            nom = patient_info.get('nom', 'Nom non disponible')
            prenom = patient_info.get('prenom', 'Prénom non disponible')
            sejours = patient_info.get('sejours', [])
            prescriptions = patient_info.get('prescriptions', [])
            avis = patient_info.get('avis', [])
        
            details = (f"Nom: {nom}\n"
                    f"Prénom: {prenom}\n\n"
                    f"Séjours:\n")
            for sejour in sejours:
                details += (f"- {sejour['date_debut']} au {sejour['date_fin']}: {sejour['motif']}\n")
            details += "\nPrescriptions:\n"
            for prescription in prescriptions:
                details += (f"- {prescription['libelle']}: {prescription['description']}\n")
            details += "\nAvis:\n"
            for avis_item in avis:
                details += (f"- {avis_item['libelle']} (Date: {avis_item['date_avis']}): {avis_item['description']}\n")
        
            self.details_text.delete(1.0, tk.END)  # Utilisez details_text au lieu de text_widget
            self.details_text.insert(tk.END, details)
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des détails du patient")


'''*
class PatientDetailsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        print("Creating patient details widgets...")
        tk.Label(self, text="Dossier du patient").pack(pady=10)
        self.details_text = tk.Text(self, height=10, width=50)
        self.details_text.pack()

    def set_patient_id(self, patient_id):
        self.load_patient_details(patient_id)
    
    def load_patient_details(self, patient_id):
        try:
            response = requests.get(config.INFO_PATIENT_URL, params={'user_id': patient_id})
            response.raise_for_status()
            data = response.json()
        
            # Assumer que la clé dans data est le nom complet du patient
            patient_name = next(iter(data))  # Récupère la première clé du dictionnaire
            patient_info = data[patient_name]  # Accède aux détails du patient
        
            print("Patient Info:", patient_info)  # Debugging line
        
            # Assurez-vous que les clés existent et utilisent des valeurs par défaut si elles sont manquantes
            nom = patient_info.get('nom', 'Nom non disponible')
            prenom = patient_info.get('prenom', 'Prénom non disponible')
            sejours = patient_info.get('sejours', [])
            prescriptions = patient_info.get('prescriptions', [])
            avis = patient_info.get('avis', [])
        
            details = (f"Nom: {nom}\n"
                    f"Prénom: {prenom}\n\n"
                    f"Séjours:\n")
            for sejour in sejours:
                details += (f"- {sejour['date_debut']} au {sejour['date_fin']}: {sejour['motif']}\n")
            details += "\nPrescriptions:\n"
            for prescription in prescriptions:
                details += (f"- {prescription['libelle']}: {prescription['description']}\n")
            details += "\nAvis:\n"
            for avis_item in avis:
                details += (f"- {avis_item['libelle']} (Date: {avis_item['date_avis']}): {avis_item['description']}\n")
        
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, details)
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            messagebox.showerror("Erreur", "Erreur lors de la récupération des détails du patient")

    
    def load_patient_details(self, patient_id):
        print(f"Loading details for patient ID: {patient_id}")
        response = requests.get(config.INFO_PATIENT_URL, params={'user_id': patient_id})
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            patient_info = response.json()
            print(f"Patient Info: {patient_info}")
            
            if isinstance(patient_info, list) and patient_info:
                patient_info = patient_info[0]

            self.details_text.delete('1.0', tk.END)
            self.details_text.insert(tk.END,
                f"Nom: {patient_info['nom']}\n"
                f"Prénom: {patient_info['prenom']}\n"
                f"Dates du séjour: {patient_info['date_debut']} - {patient_info['date_fin']}\n"
                f"Motif: {patient_info['motif']}\n"
                f"Prescriptions: {patient_info['prescriptions']}\n"
                f"Avis: {patient_info['avis']}\n"
            )
        else:
            self.details_text.delete('1.0', tk.END)
            self.details_text.insert(tk.END, "Erreur lors de la récupération des détails du patient.")
    '''