import socket, threading

def receive_messages(socket):
    while True:
        try:
            message = socket.recv(1024)
            if message:
                print(f"Message reçu : {message.decode()}")
        except:
            print("Erreur de reception de message")
            break

def send_message(socket):
    while True:
        message = input("Votre message : ")
        socket.send(message.encode("UTF-8"))

def start_client(host="127.0.0.1", port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connecté au serveur")

    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()

    send_message(client_socket)

start_client()