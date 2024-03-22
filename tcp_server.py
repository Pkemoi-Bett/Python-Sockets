#TCP server side

import socket

#Creating a server side socket using IPV4(AF_INET) and socket(SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Getting hostnames dynamically
print(socket.gethostname())  #Fetch the hostname of the device
print(socket.gethostbyname(socket.gethostname())) #Fetching the ip address of the device 


#Binding the new socket to a tuple(Ip address and Port Address)

server_socket.bind((socket.gethostbyname(socket.gethostname()), 20000))

#Puting the socket to listening mode
server_socket.listen()

#Ensuring that the server listens continously
while True:
    client_socket, client_address=server_socket.accept()
    print(client_address)
    print(type(client_address))
    print(client_socket)
    print(type(client_socket))


    print(f"Connected to {client_address}\n")

    #Sending message to the client
    client_socket.send("Hello".encode("utf-8"))

    #Closing the server side socket
    server_socket.close()
    #To terminate the loop
    break