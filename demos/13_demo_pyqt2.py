import sys  # Nécessaire pour récupérer les arguments système (sys.argv) pour QApplication
from PyQt6.QtCore import *  # Contient Qt, Qt.AlignmentFlag, signaux, slots, etc.
from PyQt6.QtGui import *   # Contient QPixmap, QFont, QPainter, etc.
from PyQt6.QtWidgets import *  # Contient tous les widgets GUI (QWidget, QPushButton, QLabel, etc.)

# --- Définition d’un widget personnalisé qui sera le contenu central ---
class MonWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # Appelle le constructeur de QWidget
        layout = QVBoxLayout()    # Layout vertical pour organiser les widgets en colonne

        # --- Label de titre ---
        label = QLabel('Mon Titre', self)  # Création d’un QLabel avec texte
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrage du texte horizontalement
        label.setGeometry(10, 10, 200, 20)  # (inutile ici car le layout gère la position)

        # --- Image ---
        imagelbl = QLabel(self)  # QLabel destiné à afficher une image
        # Charge l’image 'logo.svg' et la redimensionne à 200px de large (hauteur auto)
        imagelbl.setPixmap(QPixmap('logo.svg').scaledToWidth(200))
        imagelbl.setGeometry(10, 30, 200, 100)  # Position/Dimensions manuelles (écrasées par layout)
        imagelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centre l’image dans son QLabel
        # Style CSS appliqué au QLabel : bordure verte de 10px et fond violet
        imagelbl.setStyleSheet('border: 10px solid green; background-color: #5f68ad;')

        # --- Bouton ---
        bouton = QPushButton('OK', self)  # Bouton avec texte "OK"
        bouton.setGeometry(10, 150, 200, 20)  # Position et dimensions manuelles (inutile ici)

        # --- Ajout des widgets au layout vertical ---
        layout.addWidget(label)
        layout.addWidget(imagelbl)
        layout.addWidget(bouton)

        # Applique le layout au widget principal
        self.setLayout(layout)

# --- Définition de la fenêtre principale héritée de QMainWindow ---
class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()  # Appelle le constructeur de QMainWindow
        self.setWindowTitle('Pyqt')  # Titre affiché dans la barre de la fenêtre
        central_widget = MonWidget(self)  # Crée le widget central
        self.setCentralWidget(central_widget)  # Définit le widget comme contenu principal
        self.resize(250, 250)  # Définit la taille initiale de la fenêtre

# --- Point d’entrée de l’application ---
def main():
    app = QApplication(sys.argv)  # Crée l’objet application avec les arguments système
    fenetre = MaFenetre()         # Instancie la fenêtre principale
    fenetre.show()                # Affiche la fenêtre à l’écran
    app.exec()                    # Lance la boucle d’événements de l’application

# --- Protection du point d'entrée (exécuté uniquement si lancé en tant que script) ---
if __name__ == '__main__':
    main()
