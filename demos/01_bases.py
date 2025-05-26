# def hello_world():
#     print("Hello World !")
#     return "Hello world"

# hello_world()
# hello_world()

# # test : str = "test"

# def multiple_arg(*args):
#     print(args)

# multiple_arg(1, 2, 10, "test")

# def multiple_kwargs(**kwargs):
#     print(kwargs)

# multiple_kwargs(firstname="Toto", age=18, email="toto@email.fr")

# fct1 = lambda x : x**2

# def fct2(x):
#     return x**2

# print(fct1(2))
# print(fct2(3))

# ma_liste = [1,2,3,4,5]
# print(ma_liste[0])
# print(ma_liste[2])

# # Tuple
# def nom_prenom(nom, prenom):
#     return nom, prenom # -> packing

# resultat = nom_prenom("Toto", "Tata")
# print(resultat)
# # unpacking
# nom, prenom = resultat
# print(nom)
# print(prenom)

# def nombre():
#     return 1, 2, 3, 4, 5

# mon_tuple = nombre()
# print(mon_tuple)

# nb1, nb2, nb3, _, nb5 = mon_tuple
# print(nb3)

# for _ in range(1, 10):
#     print("hello world")

# fruits = ["Pomme", "Banane", "Pomme"]

# set_fruits = set(fruits)
# print(set_fruits)
# set_fruits.add("Poire")
# print(set_fruits)

# # Pile

# pile = []
# pile.append("premier")
# pile.append("deuxième")
# print(pile)
# pile.pop()
# print(pile)

# # file
# from collections import deque

# file = deque(["client1", "client2", "client3"])
# file.popleft()
# print(file)
# file.append("client4")
# print(file)

# # List comprehension
# ma_liste = [x for x in range(1, 26) if x % 2 == 0]
# print(ma_liste)

class CompteBancaire:
    # attributs de classe
    compteur = 0

    # def __new__(cls):
    #     cls.compteur += 1

    # Constructeur
    def __init__(self, titulaire, solde=0):
        CompteBancaire.compteur += 1
        self.titulaire = titulaire
        self.solde = solde

    def afficher_solde(self):
        print(f"Le solde de mon compte : {self.solde}")

    def __add__(self, other):
        return self.solde + other.solde

    @classmethod
    def afficher_compteur(cls):
        print(f"Nombres de compte : {cls.compteur}")

# Instanciation
compte1 = CompteBancaire("Toto", 1000)
compte2 = CompteBancaire("Tata", 100)
compte1.afficher_solde()
compte2.afficher_solde()
CompteBancaire.afficher_compteur()

print(compte1 + compte2)

print(compte1.__dict__)

# class Animal:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.age = age

#     def parler(self):
#         print(f"{self.nom} parle...")

# class Chien(Animal):
#     def __init__(self, nom, age, race):
#         super().__init__(nom, age)
#         self.race = race

#     def test(self):
#         super().parler()

# class Chat(Animal):
#     def __init__(self, nom, age, pelage):
#         super().__init__(nom, age)
#         self.pelage = pelage

# chien1 = Chien("Toto", 1, "Berger Allemand")
# chat1 = Chat("Tata", 5, "Roux")

# chien1.parler()
# chat1.parler()

from abc import ABC

class Vehicule(ABC):
    def demarrer(self):
        pass

class Electrique:
    def charger_batterie(self):
        print("Batterie en charge")

class VoitureElectrique(Vehicule, Electrique):
    def __init__(self, couleur, marque) -> None:
        # Vehicule.__init__()
        # Electrique.__init__()
        self.couleur = couleur
        self.marque = marque

    def demarrer(self): # Surcharge de méthode (polymorphisme)
        print("Véhicule électrique démarré !") 

    def __repr__(self):
        return f"Véhicule de la marque : {self.marque} de couleur {self.couleur}"

voiture = VoitureElectrique("Rouge", "Toyota")
voiture.charger_batterie()
voiture.demarrer()
print(voiture)

