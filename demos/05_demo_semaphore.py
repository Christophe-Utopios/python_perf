from threading import Thread, Semaphore
import time

# Nombre total de ressources disponibles
nb_ressources = 3

semaphore = Semaphore(nb_ressources)

def utiliser_ressource(thread_id):
    print(f"Thread {thread_id} en attente d'accès à la ressource.")
    # Acquérir la sémaphore
    semaphore.acquire()
    print(f"Thread {thread_id} accède à la ressource.")
    time.sleep(5)
    print(f"Thread {thread_id} libère la ressource")
    semaphore.release()

threads = []

for i in range(6):
    thread = Thread(target=utiliser_ressource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()