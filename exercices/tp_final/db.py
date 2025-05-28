import sqlite3

# Initialisation ou connexion à la base SQLite
def init_db():
    conn = sqlite3.connect("stats.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS resultats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_fichier TEXT,
            nb_lignes INTEGER,
            nb_mots INTEGER,
            nb_caracteres INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Insertion des données d'analyse
def inserer_statistiques(data):
    conn = sqlite3.connect("stats.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO resultats (nom_fichier, nb_lignes, nb_mots, nb_caracteres)
        VALUES (?, ?, ?, ?)
    """, (data["nom_fichier"], data["nb_lignes"], data["nb_mots"], data["nb_caracteres"]))
    conn.commit()
    conn.close()

# Affichage du contenu de la base
def afficher_stats():
    conn = sqlite3.connect("stats.db")
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM resultats"):
        print(row)
    conn.close()

# Suppression d'une ligne par ID
def supprimer_resultat(id_):
    conn = sqlite3.connect("stats.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM resultats WHERE id=?", (id_,))
    conn.commit()
    conn.close()
