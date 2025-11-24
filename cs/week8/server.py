import socket
import datetime as dt

s = socket.socket()
print("Socket created")
port = 65432

s.bind(("", port))
print("Socket binded to port %s" % (port))

s.listen()
print("listening...")
i = 1

while True:
    conn, addr = s.accept()
    print("-" * 30)
    print("Got connection from ", addr, "at %s" % (dt.datetime.now()))

    while True:
        try:
            rcvmsg = conn.recv(1024).decode()
        except ConnectionResetError:
            print("Connection reset by client")
            break
        if not rcvmsg:
            print("Client closed connection")
            break

        print(f"Received msg #{i}: '{rcvmsg}'")
        if rcvmsg in ("q", "exit"):
            sntmsg = "Server shutting down connection. Goodbye!"
            conn.send(sntmsg.encode())
            print(f"Message: '{sntmsg}' sent at {dt.datetime.now()}")
            break

        sntmsg = f"Message #{i} - '{rcvmsg}' received and ready for next message."
        conn.send(sntmsg.encode())
        print(f"'{sntmsg}' sent at {dt.datetime.now()}")
        i += 1

    conn.close()
