import socket

host = "192.168.0.25"
port = 6390

#création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host, port))

while True:
    msg = input("->")
    msg = msg.encode("utf-8")
    socket.send(msg)
    
    requete_server = socket.recv(500)
    requete_server = requete_server.decode("utf-8")
    print(requete_server)
    