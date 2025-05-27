import socket

# socket.AF_INET -> type d'adressage IPv4
# socket.SOCK_STREAM -> type de socket pour TCP (orienté connexion)
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 12345 -> port d'écoute
serveur.bind(("", 12345))

# Mise en écoute 
# liste(n) -> autorise jusqu'à n connexions
serveur.listen(1)

print("En attente d'une connexion")

# bloque jusqu'à ce qu'un client se connecte
# serveur.accept() -> retourne un tuple (socket pour cette connexion, adresse du client)
conn, addr = serveur.accept()

print(f"Connexion de {addr}")

# Réception d'un message envoyé par le client
# recv(1024) -> lit jusqu'à 1024 octets 
# bloquant par défaut (attend les données si rien reçu)
data = conn.recv(1024)

print(f"Données reçu : {data.decode()}")

# Envoie de réponse au client 
conn.sendall("Message bien reçu !".encode("UTF-8"))

# Fermeture de la connexion avec le client
conn.close()

# Fermeture du serveur
serveur.close()