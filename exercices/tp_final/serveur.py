import socket
import threading
from classes import TexteSimple
from db import inserer_statistiques
import json

# Classe gérant un client en thread
class ClientHandler(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        try:
            # On reçoit le nom et le contenu
            nom = self.client_socket.recv(1024).decode()
            contenu = self.client_socket.recv(4096).decode()

            # On crée un objet Fichier et on l'analyse
            fichier = TexteSimple(nom, contenu)
            resultats = fichier.analyser()

            # Enregistrement en BDD
            inserer_statistiques(resultats)

            # Sauvegarde JSON (append)
            with open("logs.json", "a") as f:
                json.dump(resultats, f)
                f.write("\n")

            # Réponse au client
            self.client_socket.send(b"Fichier traite et stocke.\n")
        except Exception as e:
            self.client_socket.send(f"Erreur: {e}".encode())
        finally:
            self.client_socket.close()

# Lancement du serveur TCP
def lancer_serveur():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(("localhost", 8888))
    serveur.listen(5)
    print("Serveur en écoute sur le port 8888")

    while True:
        client_socket, _ = serveur.accept()
        handler = ClientHandler(client_socket)
        handler.start()
