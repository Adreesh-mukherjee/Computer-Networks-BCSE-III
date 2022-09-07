import socket

port = 8080
host = socket.gethostbyname(socket.gethostname())

addr = (host,port)

s = socket.socket()

s.connect((addr))
while True:
    data = str(input("data to send: "))
    s.send(data.encode())
    if data=="q":
        break
s.close()    