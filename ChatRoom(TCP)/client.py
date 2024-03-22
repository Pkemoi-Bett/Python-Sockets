import threading 
import socket

host = socket.gethostbyname(socket.gethostname())
port = 20000
encoder = "utf-8"
bytesize = 1024

username = input("Enter your username:\n")

# Creating client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(bytesize).decode(encoder)
            if message == "user":
                client.send(username.encode(encoder))
            else:
                print(message)
        except:
            print("An Error Occurred!!")
            client.close()
            break

def write():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode(encoder))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
