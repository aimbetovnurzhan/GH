import socket

s = socket.socket()

port = 65432

s.connect(("127.0.0.1", port))

while True:
    msg = input("Введите сообщение (или 'exit'): ")
    if msg == "exit":
        break
    s.sendall(msg.encode())

print(s.recv(1024).decode())
s.close()