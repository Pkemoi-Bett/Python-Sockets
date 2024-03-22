#Chat Client Side 

import socket

#Declearing Constants 
DEST_IP=socket.gethostbyname(socket.gethostname())
DEST_PORT=20000
ENCODER="utf-8"
BYTESIZE=1024


#Creating client socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

#Send and receive information
while True:
    #Receive information from the server
    message=client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if the server wants to quit else continue sending messages
    if message=="quit":
        client_socket.send("quit".encode(ENCODER))
        print("\n Quiting the conversation")
        break

    else:
        print(f"\n{message}")
        message=input("Message:  ")
        client_socket.send(message.encode(ENCODER))


#Closing the client Socket
        
client_socket.close()