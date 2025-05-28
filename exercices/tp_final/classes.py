from abc import ABC, abstractmethod

# Classe abstraite de base pour les fichiers
class Fichier(ABC):
    def __init__(self, nom, contenu):
        self.nom = nom
        self.contenu = contenu

    @abstractmethod
    def analyser(self):
        pass

    def __str__(self):
        return f"{self.nom} - {len(self.contenu)} caractères"

    def __len__(self):
        return len(self.contenu)

    def __eq__(self, other):
        return isinstance(other, Fichier) and self.nom == other.nom

# Fichier texte standard : compte lignes, mots, caractères
class TexteSimple(Fichier):
    def analyser(self):
        lignes = self.contenu.splitlines()
        mots = self.contenu.split()
        return {
            "nom_fichier": self.nom,
            "nb_lignes": len(lignes),
            "nb_mots": len(mots),
            "nb_caracteres": len(self.contenu)
        }

# Fichier de code Python : compte fonctions, classes, commentaires
class TexteCode(Fichier):
    def analyser(self):
        lignes = self.contenu.splitlines()
        fonctions = [l for l in lignes if l.strip().startswith("def ")]
        classes = [l for l in lignes if l.strip().startswith("class ")]
        commentaires = [l for l in lignes if l.strip().startswith("#")]
        return {
            "nom_fichier": self.nom,
            "nb_lignes": len(lignes),
            "nb_fonctions": len(fonctions),
            "nb_classes": len(classes),
            "nb_commentaires": len(commentaires)
        }
