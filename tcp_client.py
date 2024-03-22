#TCP CLIENT SIDE

import socket

#Creating a client side socket using IPV4(AF_INET) and socket(SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Connecting the cliet side to server side using IP an Port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 20000))

#Recieving message from the server side 
#You must specify the max no of bytes to receive
message=client_socket.recv(1024)

print(message.decode("utf-8"))

#Closing the client side socket
client_socket.close()