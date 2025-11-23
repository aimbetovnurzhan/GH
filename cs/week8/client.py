import socket

host = "127.0.0.1"
port = 65432

with socket.socket() as s:
    s.connect((host, port))
    while True:
        sntmsg = input("Enter message for sending:")
        s.send(sntmsg.encode())
        print(s.recv(1024).decode())
        if sntmsg in ("exit", "q"):
            break