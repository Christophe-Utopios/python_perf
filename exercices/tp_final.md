# TP de Fin de Formation – Python Perfectionnement

## Objectif

Développer une application en ligne de commande capable de recevoir, analyser et stocker des fichiers texte envoyés par des clients via réseau.

---

## Contexte

L'application sera construite autour de plusieurs modules Python, exploitant les notions suivantes :

- Programmation orientée objet avec héritage
- Communication réseau avec `socket`
- Exécution parallèle avec `threading`
- Sauvegarde structurée avec SQLite et JSON
- Interface console pour l’interaction utilisateur

---

## Consignes

### 1. Programmation Orientée Objet

- Créer une classe abstraite `Fichier` avec :

  - `__init__(nom, contenu)` : initialise le nom et le contenu du fichier
  - `analyser()` : méthode abstraite à redéfinir dans les sous-classes
  - Méthodes dunder :
    - `__str__` : retourne un résumé du fichier
    - `__eq__` : compare deux fichiers par nom
    - `__len__` : retourne la longueur du contenu

- Implémenter deux sous-classes :
  - `TexteSimple` : compte lignes, mots, caractères
  - `TexteCode` : compte fonctions, classes, commentaires

---

### 2. Traitement de fichiers

- Le contenu du fichier est analysé selon son type.
- Les résultats sont retournés sous forme de dictionnaire :
  ```python
  {
    "nom_fichier": "exemple.txt",
    "nb_lignes": 4,
    "nb_mots": 12,
    "nb_caracteres": 98
  }
  ```

### 3. Multi-threading

- Utiliser la classe threading.Thread pour gérer chaque client dans un thread séparé.

- Créer une classe ClientHandler(Thread) :
  - Reçoit un fichier
  - Lance l’analyse
  - Stocke les résultats

### 4. Communication Réseau

- Créer un serveur TCP :
  - Port : localhost:8888
  - Écoute les connexions clients
  - Reçoit deux messages :
    - Le nom du fichier
    - Le contenu du fichier

### 5. Sauvegarde SQLite

- Base : stats.db
- Table : resultats
  - nom_fichier (TEXT)
  - nb_lignes (INT)
  - nb_mots (INT)
  - nb_caracteres (INT)
- Insérer une nouvelle ligne à chaque analyse

### 6. Interface Console

- Affichage d’un menu :

```bash
1. Afficher les résultats
2. Supprimer un résultat
3. Quitter
```

- Affichage via SELECT

- Suppression par ID

### 7. Journalisation JSON

- Chaque analyse est également ajoutée ligne par ligne à un fichier logs.json
- Format : dictionnaire JSON sérialisé

### Fichiers attendus

main.py : point d’entrée, lance le serveur et le menu
classes.py : définitions des classes et logique d’analyse
serveur.py : serveur TCP et gestion des connexions multithread
db.py : création et manipulation de la base SQLite
client.py : client de test simulant un envoi de fichier
logs.json : historique sérialisé des analyses
stats.db : base de données SQLite locale
