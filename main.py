import tkinter as tk
from login_page import LoginPage
from dashboard_page import DashboardPage
from patient_details_page import PatientDetailsPage
import config  # Importez le fichier de configuration

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App Bureatique")
        self.geometry("600x400")
        self.frames = {}
        self.create_frames()

    def create_frames(self):
        print("Creating frames...")
        self.frames['login'] = LoginPage(self, self.show_dashboard)
        self.frames['dashboard'] = DashboardPage(self, self.show_patient_details)
        self.frames['patient_details'] = PatientDetailsPage(self)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('login')

    def show_frame(self, page_name):
        print(f"Showing frame: {page_name}")
        frame = self.frames[page_name]
        frame.tkraise()

    def show_dashboard(self):
        self.show_frame('dashboard')

    def show_patient_details(self, patient_id):
        self.frames['patient_details'].set_patient_id(patient_id)
        self.show_frame('patient_details')

app = App()
app.mainloop()
