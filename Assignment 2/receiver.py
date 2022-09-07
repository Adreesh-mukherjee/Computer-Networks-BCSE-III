import socket
import time

port = 8080
host = socket.gethostbyname(socket.gethostname())

addr = (host,port)

s = socket.socket()

s.bind((addr))
s.listen()
conn,address = s.accept()
print("Connected to address: ",address)
while True:
    
    msg = conn.recv(1024).decode()
    if msg == "q":
        break
    print(msg)
s.close()    