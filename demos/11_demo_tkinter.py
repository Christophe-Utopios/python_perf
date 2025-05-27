import tkinter as tk
from tkinter import messagebox

# Création de la fenêtre principale
fenetre = tk.Tk() # Instancie une fenêtre vide
fenetre.title('Application démo') # Titre affiché dans la barre de la fenêtre
fenetre.geometry("300x150") # Définit la taille de la fenêtre largeurxhauteur

# Création d'un widget
label = tk.Label(fenetre, text="Je suis un widget") # Création d'un widget avec un texte
label.pack(pady=10) # Ajoute le label à la fenêtre avec un espacement (vertical) de 10px

def saluer():
    messagebox.showwarning("Bonjour tout le monde !")

# Création d'un bouton
bouton = tk.Button(fenetre, text="Clique ici !", command=saluer)
bouton.pack(pady=10)

fenetre.mainloop() # Bloque jusqu'à la fermeture de la fenêtre