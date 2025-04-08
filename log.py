import tkinter as tk
from tkinter import messagebox

users = {}

def register():
    username = entry_username.get() 
    password = entry_password.get()
    
    if username in users:
        messagebox.showerror("Błąd", "Użytkownik już istnieje. Wybierz inną nazwę.")
    else:
        users[username] = password
        messagebox.showinfo("Sukces", "Rejestracja zakończona pomyślnie!")

def login():
    username = entry_username.get()
    password = entry_password.get() 

    if username in users and users[username] == password:
        messagebox.showinfo("Sukces", "Logowanie zakończone pomyślnie!")
    else:
        messagebox.showerror("Błąd", "Błędna nazwa użytkownika lub hasło.")

root = tk.Tk()
root.title("System Logowania")

label_username = tk.Label(root, text="Nazwa użytkownika:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Hasło:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_register = tk.Button(root, text="Rejestracja", command=register)
button_register.pack()

button_login = tk.Button(root, text="Logowanie", command=login)
button_login.pack()

root.mainloop()