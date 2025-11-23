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
    i = 1
    conn, addr = s.accept()
    print("Got connection from ", addr, "at %s" % (dt.datetime.now()))
    rcvmsg = conn.recv(1024).decode()
    print(f"Received msg #{i}: '{rcvmsg}'")
    sntmsg = "Thanks for connection"
    conn.send(sntmsg.encode())
    print(f"Message '{sntmsg}' sent at {dt.datetime.now()}")
    conn.close()
    i += 1
    if rcvmsg in ("q", "exit"):
        break