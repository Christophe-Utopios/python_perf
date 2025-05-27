import socket, threading

clients = []

def handle_client(client_socket, address):
    print(f"NOUVELLE CONNEXION : {address} est connecté !")

    while True:
        try:
            message = client_socket.recv(1024)

            if not message:
                break

            print(f"{address} : {message.decode()}")

            for client in clients:
                if client != client_socket: # On évite de renvoyer à l'émetteur
                    client.send(message)
        except:
            break
    
    print(f"Déconnexion de {address}")
    clients.remove(client_socket)
    client_socket.close()

def start_server(host="127.0.0.1", port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Serveur en écoute {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket, addr,), daemon=True)
        thread.start()

start_server()