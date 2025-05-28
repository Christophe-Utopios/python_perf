from flask_sqlalchemy import SQLAlchemy # pip install flask_sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost/demo_python', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

# Création de la table
# Base.metadata.create_all(engine)

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

# user1 = User(name="Toto", email='toto@email.fr')
# user2 = User(name="Tata", email='tata@email.fr')
# session.add_all([user1, user2])
# session.commit()

# Read
users = session.query(User).all()
for user in users:
    print(user.name, user.email)

session.close()