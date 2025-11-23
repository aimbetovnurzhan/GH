import socket
import datetime as dt

s = socket.socket()
print("Socket created")
port = 65432

s.bind(("", port))
print("Socket binded to port %s" % (port))

s.listen()
print("listening...")

while True:
    conn, addr = s.accept()
    print("Got connection from ", addr)
    print("Received msg:", conn.recv(1024).decode())
    msg = "Thanks for connection "
    conn.send(msg.encode())
    print(f"Message {msg} sent at {dt.datetime.now()}")
    conn.close()
    break