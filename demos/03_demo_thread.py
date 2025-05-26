# Méthode 1 : sans utiliser de classe
from collections.abc import Callable
from threading import Thread
import time
from typing import Iterable, Mapping

def tache_simple(nom):
    for i in range(3):
        print(f"{nom} itération : {i}")
        time.sleep(1)

# Création des threads
# t1 = Thread(target=tache_simple, args=("Thread1",))
# t2 = Thread(target=tache_simple, args=("Thread2",))

# Démarrage des threads
# t1.start()
# t2.start()

# Attendre la fin d'un thread
# t1.join()

# print("Suite de mon code.")

# Méthode 2 : Avec sous-classe

# class MonThread(Thread):
#     def __init__(self, nom):
#         super().__init__()
#         self.nom = nom

#     def run(self):
#         for i in range(3):
#             print(f"{self.nom} itération : {i}")
#             time.sleep(1)

# Création du thread :
# t1 = MonThread("Thread1")
# t2 = MonThread("Thread2")

# Démarrage des threads
# t1.start()
# t2.start()

# Méthode 3 : sans sous-classe

class MonThread:
    def __init__(self, nom) -> None:
        self.nom = nom

    def tache_simple(self):
        for i in range(3):
            print(f"{self.nom} itération : {i}")
            time.sleep(1)
    
    def tache_simple2(self):
        for i in range(3):
            print(f"{self.nom} itération : {i}")
            time.sleep(1)

obj1 = MonThread("Thread1")
t1 = Thread(target=obj1.tache_simple)
t2 = Thread(target=obj1.tache_simple2)

t1.start()
t2.start()