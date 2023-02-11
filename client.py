import socket
from threading import Thread

def Send(client):
    while True:
        msg = input("->")
        msg = msg.encode("utf-8")
        socket.send(msg)

def Receive(client):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")
        print(requete_server)
        
host = "192.168.0.25"
port = 6390

#création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host, port))

envoi = Thread(target=Send,args=[client])
reception = Thread(target=Receive,args=[client])

envoi.start()
reception.start()
