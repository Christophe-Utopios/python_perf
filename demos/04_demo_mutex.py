from threading import Thread, Lock
import time

compteur = 0
verrou = Lock()

def incrementer():
    global compteur
    for _ in range(1000):
        with verrou:
            compteur += 1

t1 = Thread(target=incrementer)
t2 = Thread(target=incrementer)

t1.start()
t2.start()

t1.join()
t2.join()

print(compteur)