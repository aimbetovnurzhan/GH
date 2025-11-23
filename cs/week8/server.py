import socket

s = socket.socket()
print("Socket created")

port = 65432

s.bind(("", port))
print("Socket binded to port %s" % (port))

s.listen()
print("listening...")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print("Got connection from ", addr)
    conn.send("Thanks for connection ".encode())
    print("Получено:", data.decode())
    conn.send("Принято: ", data)

    c.close()

    break