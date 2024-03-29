import sqlalchemy as db
import pymysql
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
#criar o engine ou motor de ligação com o sql
engine = db.create_engine('mysql+pymysql://root@localhost:3306/hortifruti')
#trazendo a declaração de objetos no sqlalchemy
Base = declarative_base()

#objeto recebendo a informação do tipo de coluna
class Fruta(Base):
    __tablename__ = 'Frutas'
    id =Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(60),nullable=False)
    cor_principal = Column(String(60))

#criar as tebelas dos objetos criados
Base.metadata.create_all(engine)
#criar a seção e linkar com o engine
Session = sessionmaker(bind=engine)
session = Session()
#menu para criação recebendo do usuario e comitando para o sql
'''op = 1
while op != 0:
    nome_fruta = input('digite o nome da fruta: ')
    cor_fruta = input(f'digite a cor da {nome_fruta}: ')
    fruta=Fruta(nome=nome_fruta,cor_principal=cor_fruta)
    session.add(fruta)
    session.commit()
    op = int(input('deseja continuar [0] para Parar:\n [1] para Continuar: '))'''

#menu de visualização da tabela
'''consulta = session.query(Fruta).all()
for Fruta in consulta:
    print(Fruta.id,Fruta.nome,Fruta.cor_principal)'''

#menu de alteração de itens
consulta = session.query(Fruta).filter(Fruta.id == 1).first()
consulta.nome='maçã'
session.add(consulta)
session.commit()

#menu para deletar itens
consulta = session.query(Fruta).filter(Fruta.id == 1).first()
session.delete(consulta)
session.commit()
