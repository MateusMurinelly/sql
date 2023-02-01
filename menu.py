import sqlalchemy as db
import pymysql
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
#criar o engine ou motor de ligação com o sql
engine = db.create_engine('mysql+pymysql://root@localhost:3306/livros')
#trazendo a declaração de objetos no sqlalchemy
Base = declarative_base()

#objeto recebendo a informação do tipo de coluna
class livros(Base):
    __tablename__ = 'Livros'
    id = Column(Integer,primary_key=True,autoincrement=True)
    titulo = Column(String(60),nullable=False)


#criar as tebelas dos objetos criados
Base.metadata.create_all(engine)
#criar a seção e linkar com o engine
Session = sessionmaker(bind=engine)
session = Session()

op = int(input('digite qual a opção desejada [1]criar novo item\n [2]visualizar itens existentes\n [3]alterar itens existentes\n [4]deletar itens\n [5]sair:'))
while op !=6:
    if op == 1:
        #menu para criação recebendo do usuario e comitando para o sql
        Nome_livro = input('Digite o nome do livro que deseja acrescentar ao banco: ')
        Livro = livros(titulo=Nome_livro)
        session.add(Livro)
        session.commit()
        op = int(input(
            'digite qual a opção desejada [1]criar novo item\n [2]visualizar itens existentes\n [3]alterar itens existentes\n [4]deletar itens\n [5]sair:'))

    elif op == 2:
        #menu de visualização da tabela
        consulta = session.query(livros).all()
        for Livro in consulta:
            print(Livro.id,'|',Livro.titulo)
        op = int(input(
            'digite qual a opção desejada [1]criar novo item\n [2]visualizar itens existentes\n [3]alterar itens existentes\n [4]deletar itens\n [5]sair:'))

    elif op == 3:
        #menu de alteração de itens
        lista_titulos = session.query(livros).all()
        for Livro in lista_titulos:
            print(Livro.id,'|',Livro.titulo)
        id_lista = int(input('digite o numero de id do livro que deseja alterar: '))
        consulta = session.query(livros).filter(livros.id == id_lista).first()
        novo_Titulo = input('digite o novo titulo: ')
        consulta.titulo=novo_Titulo
        session.add(consulta)
        session.commit()
        op = int(input(
            'digite qual a opção desejada [1]criar novo item\n [2]visualizar itens existentes\n [3]alterar itens existentes\n [4]deletar itens\n [5]sair:'))

    elif op == 4:
        #menu para deletar itens
        lista_livros = session.query(livros).all()
        for Livro in lista_livros:
            print(Livro.id,'|',Livro.titulo)
        id_listad = int(input('digite o numero de id do livro que deseja deletar: '))
        consulta = session.query(livros).filter(livros.id == id_listad).first()
        session.delete(consulta)
        session.commit()
        op = int(input(
            'digite qual a opção desejada [1]criar novo item\n [2]visualizar itens existentes\n [3]alterar itens existentes\n [4]deletar itens\n [5]sair:'))

    elif op == 5:
        print('até depois')
        op = 6