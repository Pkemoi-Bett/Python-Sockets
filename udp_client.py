#UDP client side 

import socket

#Creating UDP client side using IPV4(AF_INET) and SOCKET(DGRAM)

client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Sending information

client_socket.sendto("Hello".encode("utf-8"),(socket.gethostbyname(socket.gethostname()), 20000))