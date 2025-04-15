#Aim:Write a python program to create simple socket for file sending between server and client.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03


import socket
import os
HOST = '127.0.0.1'
PORT = 56789
file_name = "smaple.txt"
if not os.path.exists(file_name):
    print(f"Error: File '{file_name}' not found.")
    exit()
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.send(file_name.encode())
    with open(file_name, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)
    print(f"File '{file_name}' sent successfully.")
except ConnectionRefusedError:
    print("Error: Server is not running or refused connection.")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied for '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    client_socket.close()
