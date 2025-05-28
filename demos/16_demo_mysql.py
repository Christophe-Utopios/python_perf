import mysql.connector # pip install mysql-connector-python

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo_python"
)

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personnes (
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               age INT);''')

personnes = [
    ("Toto", 25),
    ("Tata", 30),
    ("Titi", 35),
]

# cursor.executemany("INSERT INTO personnes (name, age) VALUES (%s, %s)", personnes)

connection.commit()

cursor.execute("SELECT * FROM personnes")
for row in cursor.fetchall():
    print(row)

connection.close()