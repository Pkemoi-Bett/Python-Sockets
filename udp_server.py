#UDP SERVER SIDE

import socket

#Creating UDP socket using IPV4(AF_INET) and socket(SOCK_DGRAM)
server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Binding the UDP server side(IP address and Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 20000))


#In UDP we do not create listen method because it is a connectionless protocol
message, address=server_socket.recvfrom(1024)
print(message.decode("utf-8"))
#print(message)