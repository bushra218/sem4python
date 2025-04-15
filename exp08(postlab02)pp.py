#Aim:Write a Python GUI password protected program
# Branch: Comps Year: SE
# Sem: IV Subject: Python
# Name:Ansari Bushra UIN: 231P046 Roll No: 03
import tkinter as tk
from tkinter import messagebox

PASSWORD = "Bush1407"
def check_password():
    entered_password = entry_password.get()
    if entered_password == PASSWORD:
        messagebox.showinfo("Success", "Access Granted!")
        root.destroy()
        open_main_app()
    else:
        messagebox.showerror("Error", "Incorrect Password!")
def open_main_app():
    main_app = tk.Tk()
    main_app.title("Main Application")
    main_app.geometry("300x200")
    
    label = tk.Label(main_app, text="Welcome to the Main Application!", font=("Arial", 12))
    label.pack(pady=20)
    
    btn_exit = tk.Button(main_app, text="Exit", command=main_app.destroy)
    btn_exit.pack(pady=10)

    main_app.mainloop()
root = tk.Tk()
root.title("Password Protected")
root.geometry("300x150")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=5)

entry_password = tk.Entry(root, width=20, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=check_password)
btn_login.pack(pady=10)

root.mainloop()
