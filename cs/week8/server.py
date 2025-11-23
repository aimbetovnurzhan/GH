import socket

s = socket.socket()
print("Socket successfully created")

port = 65432

s.bind(("", port))
print("Socket binded to %s" % (port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection form ", addr)

    c.send("Thanks for connection ".encode())
    c.close()
    