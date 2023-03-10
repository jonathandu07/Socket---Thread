import socket
from threading import Thread

def Send(client):
    while True:
        msg = input("->")
        msg = msg.decode("utf-8")
        client.send(msg)

def Receive(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode("utf-8")
        print(requete_client)
        if not requete_client: #Si on perd la connexion
            print("le client s'est déconnecté")
            break
        
host = "192.168.0.25"
port = 6390

#création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((host, port))
socket.listen(1)

#Le script s'arrête jusqu'a une connection
client, ip = socket.accept()
print("le client :",ip,"s'est connecté")

envoi = Thread(target=Send,args=[client])
reception = Thread(target=Receive,args=[client])

envoi.start()
reception.start()

reception.join()

client.close()
socket.close()
    