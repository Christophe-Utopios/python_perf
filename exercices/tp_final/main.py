from db import init_db, afficher_stats, supprimer_resultat
from serveur import lancer_serveur
import threading

# Lancer serveur dans un daemon thread
def start_server():
    thread = threading.Thread(target=lancer_serveur, daemon=True)
    thread.start()

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Afficher les statistiques")
        print("2. Supprimer un résultat")
        print("3. Quitter")
        choix = input("Choix : ")
        if choix == "1":
            afficher_stats()
        elif choix == "2":
            id_ = input("ID à supprimer : ")
            supprimer_resultat(int(id_))
        elif choix == "3":
            break

if __name__ == "__main__":
    init_db()
    start_server()
    menu()
