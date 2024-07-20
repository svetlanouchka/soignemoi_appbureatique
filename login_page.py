import tkinter as tk
import requests
from tkinter import messagebox
import config  # Importez le fichier de configuration

class LoginPage(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.parent = parent
        self.on_login_success = on_login_success
        self.create_widgets()

    def create_widgets(self):
        print("Creating login widgets...")
        tk.Label(self, text="Login").pack(pady=10)
        tk.Label(self, text="Email").pack()
        self.email = tk.Entry(self)
        self.email.pack()

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show='*')
        self.password.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)

    def login(self):
        print("Attempting to login...")
        email = self.email.get()
        password = self.password.get()
        print(f"Email: {email}, Password: {password}")

        login_data = {
            'email': email,
            'password': password
        }
        print(f"Data being sent: {login_data}"
        )
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(config.LOGIN_URL, json=login_data, headers=headers)
        if response.status_code == 200:
            print("Login successful")
            # Process successful login
            self.on_login_success()
        else:
            print("Login failed")
            messagebox.showerror("Login Error", "Invalid email or password.")
