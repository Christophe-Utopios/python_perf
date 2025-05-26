import random        # Module pour générer des nombres aléatoires
import queue         # Module pour créer une file d'attente thread-safe
import threading     # Module pour gérer les threads

# Classe Producteur : hérite de threading.Thread
class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)  # Initialisation de la classe Thread parente
        self.queue = queue               # Référence à la file d'attente partagée

    def run(self):
        # Boucle de production : produit 10 nombres aléatoires
        for x in range(10):
            number = random.randint(1, 1000)  # Génère un entier aléatoire entre 1 et 1000
            self.queue.put(number)           # Place le nombre dans la file d'attente (opération thread-safe)
            print(f"prod {number}")          # Affiche le nombre produit
        self.queue.put(0)  # Envoie un "signal de terminaison" pour le consommateur (valeur spéciale)

# Classe Consommateur : hérite de threading.Thread
class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)  # Initialisation de la classe Thread parente
        self.queue = queue               # Référence à la file d'attente partagée

    def run(self):
        while True:                          # Boucle infinie de consommation
            number = self.queue.get()        # Récupère un élément de la file (bloquant si vide)
            if number == 0:                  # Si le signal de terminaison est reçu
                break                        # Sort de la boucle
            print(f"Nombre consommé :  {number}")  # Affiche le nombre consommé
            self.queue.task_done()          # Indique que la tâche a été traitée (utile si on appelle join sur la file)

# Fonction principale
def main():
    q = queue.Queue()          # Crée une file d'attente thread-safe
    prod = Producer(q)         # Instancie un producteur avec la file
    cons = Consumer(q)         # Instancie un consommateur avec la file
    prod.start()               # Démarre le thread producteur
    cons.start()               # Démarre le thread consommateur
    prod.join()                # Attend la fin du thread producteur
    cons.join()                # Attend la fin du thread consommateur

main()  # Appel de la fonction principale
