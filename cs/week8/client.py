import socket

s = socket.socket()
port = 65432

while True:
    s.connect(("127.0.0.1", port))
    s.send("Test connection".encode())
    print(s.recv(1024).decode())
    s.close()
    break