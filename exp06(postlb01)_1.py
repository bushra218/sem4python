#Aim:Write a python program to create simple socket for basic information exchange between server
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03
import socket
HOST = '127.0.0.1'
PORT = 12345
print("Starting server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")
while True:
    data = client_socket.recv(1024).decode()
    print(f"Client: {data}")
    if data.lower() == "bye":
        break
    server_message = input("Server: ")
    client_socket.send(server_message.encode())
    if server_message.lower() == "bye":
        break
client_socket.close()
server_socket.close()
print("Server closed.")
