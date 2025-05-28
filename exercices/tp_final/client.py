import socket

# Simulation d'un fichier texte
nom_fichier = "exemple.txt"
contenu = """Bonjour,
Ceci est un fichier de test.
Il contient plusieurs lignes,
et des mots à analyser."""

# Connexion au serveur (doit être déjà en écoute sur localhost:8888)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8888))

# Envoi du nom du fichier (encodé)
client.send(nom_fichier.encode())

# Pause très courte pour éviter une collision d'envoi
import time
time.sleep(0.1)

# Envoi du contenu du fichier
client.send(contenu.encode())

# Réception du message du serveur
reponse = client.recv(1024)
print("Réponse du serveur :", reponse.decode())

client.close()
