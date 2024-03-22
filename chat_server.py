#Chat Server Side

import socket

#Declaring constanst
HOST_IP=socket.gethostbyname(socket.gethostname())
HOST_PORT=20000
ENCONDER="utf-8"
BYTESIZE=1024

#Creating chat server socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT)) #Binding the server socket to host IP and Host port
server_socket.listen()


#Accepting incoming connection and let the client side know that they are connected

print("Server is Running.....\n")
client_socket, client_address=server_socket.accept()
client_socket.send("You are connected to the server...\n".encode(ENCONDER))



#Sending and receiving messages

while True:
    #Receiving message from the client
    message=client_socket.recv(BYTESIZE).decode(ENCONDER)

    #Quit if the cliebt want to quit else continue
    if message == "quit":
        client_socket.send("quit".encode(ENCONDER))
        print("\n Quiting the chat....... Goodbye!")
        break

    else:
        print(f"\n {message}")
        message=input("Message: ")
        client_socket.send(message.encode(ENCONDER))


#Closing chat Server
server_socket.close()
