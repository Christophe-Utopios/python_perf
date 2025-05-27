from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
# Import des composants principaux de PyQt6 pour créer une interface graphique :
# - QApplication : point d'entrée de l'application
# - QWidget : conteneur de base (fenêtre ou sous-fenêtre)
# - QLabel : composant d'affichage de texte
# - QVBoxLayout : layout vertical
# - QPushButton : bouton cliquable

# --- Création de l'application ---
# QApplication([]) : initialise l’environnement graphique
# La liste vide simule les arguments de la ligne de commande
app = QApplication([])

# --- Création de la fenêtre principale ---
fenetre = QWidget()  # QWidget est une fenêtre vide de base
fenetre.setWindowTitle("Ma première application PyQt6")  # Titre de la fenêtre
fenetre.resize(300,150)  # Taille initiale de la fenêtre (largeur x hauteur)

# --- Création d’un layout vertical ---
layout = QVBoxLayout()  # Permet d’empiler les widgets verticalement

# --- Fonction appelée lors du clic sur le bouton ---
def direBonjour(): 
    # Modifie dynamiquement le texte du 3e label
    label3.setText("Bnjour après click")

# --- Ajout des widgets ---
label1 = QLabel("Bonjour, PyQt6!")  # Label affichant un texte fixe
label2 = QLabel("Bonjour, PyQt6!")  # Deuxième label identique
label3 = QLabel()                   # Label vide (sera rempli après clic)

button1 = QPushButton("Dire bonjour")  # Bouton avec texte affiché
button1.clicked.connect(direBonjour)   # Connexion du clic du bouton à la fonction direBonjour

# Ajout de tous les widgets au layout (ordre vertical)
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(button1)
layout.addWidget(label3)

# --- Application du layout à la fenêtre ---
fenetre.setLayout(layout)

# --- Affichage de la fenêtre ---
fenetre.show()

# --- Lancement de la boucle principale ---
# app.exec() : boucle d’événements de l’interface, traite les actions utilisateur
app.exec()
