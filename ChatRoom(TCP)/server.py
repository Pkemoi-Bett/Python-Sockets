import threading 

import socket

host=socket.gethostbyname(socket.gethostname())
port=20000
encoder="utf-8"
bytesize=1024

#Creating the  server socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#Creating empty list of clients and usernames
clients=[]
usernames=[]

#creating a broadcast function
def broadcast(message):
    for client in clients:
        client.send(message.encode(encoder))

#function to handle clients session
def handle(client):
    while True:
        try:
            message = client.recv(bytesize).decode(encoder)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chat")
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send("user".encode(encoder))
        username = client.recv(bytesize).decode(encoder)
        usernames.append(username)
        clients.append(client)
        print(f"Username of the client is {username}")
        broadcast(f"{username} joined the chat!")
        client.send("Connected to the server".encode(encoder))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()

          

         



