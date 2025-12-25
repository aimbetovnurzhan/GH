import socket

host = "127.0.0.1"
port = 65432
with socket.socket() as s:
    s.connect((host, port))
    print("Connected to server")

    while True:
        sntmsg = input("Enter message for sending (q/exit to quit):")
        s.send(sntmsg.encode())

        print("server response:", s.recv(1024).decode())
        if sntmsg in ("exit", "q"):
            break

print("Connection closed")