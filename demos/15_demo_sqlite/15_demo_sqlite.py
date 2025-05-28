import sqlite3

db_file = "./demos/15_demo_sqlite/testdb.sqlite"

# Connexion à notre bdd sqlite
connection = sqlite3.connect(db_file)

# Création d'un curseur
cursor = connection.cursor()

# Création d'une table personnes (Create)
cursor.execute('''CREATE TABLE IF NOT EXISTS personnes(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER
               );''')

personnes = [
    ('Toto', 30),
    ('Tata', 25),
    ('Titi', 18)
]

# Insertion de quelques données (Create)
# cursor.executemany('INSERT INTO personnes (name, age) VALUES (?, ?)', personnes)

# Suppression d'une personne (Delete)
# cursor.execute('DELETE FROM personnes WHERE id = ?', (2,))

# Modification d'une personne (Update)
# cursor.execute('UPDATE personnes SET name = ?, age = ? WHERE id = ?', ("Tutu", 26, 3))

# Valider les requêtes
connection.commit()

# Récupérer des données (Read)
cursor.execute('SELECT * FROM personnes')
print("Données dans la table personnes :")
for row in cursor.fetchall():
    print(row)

# Fermeture de la connexion
connection.close()