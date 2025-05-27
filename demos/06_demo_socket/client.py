import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 12345))

client.sendall("Bonjour serveur".encode('UTF-8'))

reponse = client.recv(1024)
print(f"Réponse : {reponse.decode()}")

client.close()