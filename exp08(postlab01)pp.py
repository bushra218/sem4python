""" Aim:Write a Python program to create entry widgets for entering user name and 
password and display entered text"""
# Branch: Comps Year: SE
# Sem: IV Subject: Python
# Name:Ansari Bushra  UIN: 231P046  Roll No: 03
import tkinter as tk
from tkinter import messagebox

def show_entries():
    username = entry_username.get()
    password = entry_password.get()
    messagebox.showinfo("Entered Details", f"Username: {username}\nPassword: {password}")

root = tk.Tk()
root.title("User Login Form")
root.geometry("300x200")

# Username Label and Entry
label_username = tk.Label(root, text="Username:", font=("Arial", 12))
label_username.pack(pady=5)
entry_username = tk.Entry(root, width=25)
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(root, text="Password:", font=("Arial", 12))
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=25, show="*")  # Hides password input
entry_password.pack(pady=5)

# Button to Show Entered Data
btn_submit = tk.Button(root, text="Submit", command=show_entries)
btn_submit.pack(pady=10)

root.mainloop()

