import sqlalchemy as db
import pymysql
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base


engine = db.create_engine('mysql+pymysql://root:@localhost:3306/aula02')
Base = declarative_base()


class Friends(Base):
    __tablename__ = 'friends'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(60))
    personagem = Column(String(60))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


Rachel=Friends(
    nome = 'Jennifer Aniston ',
    personagem = 'Rachel Green')
Monica=Friends(
    nome= 'Courteney Cox ',
    personagem= 'Monica Geller')
Phoebe=Friends(
    nome= 'Lisa Kudrow',
    personagem='Phoebe Buffay')
Joey=Friends(
    nome= 'Matt LeBlanc',
    personagem= 'Joey Tribbiani')
Chandler=Friends(
    nome= 'Matthew Perry ',
    personagem= 'Chandler Bing')
Ross=Friends(
    nome= 'David Schwimmer ',
    personagem= 'Ross Geller ')

session.add_all([Rachel,Monica,Phoebe,Joey,Chandler,Ross])
session.commit()
