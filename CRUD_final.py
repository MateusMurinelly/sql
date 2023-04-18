import sqlalchemy as db
import pymysql
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import tkinter as tk
from tkinter import *
from tkinter import messagebox


# criar o engine ou motor de ligação com o sql
engine = db.create_engine('mysql+pymysql://root:123456@localhost:3306/cadastro')
# trazendo a declaração de objetos no sqlalchemy
Base = declarative_base()

# objeto recebendo a informação do tipo de coluna
class Cadastro(Base):
    __tablename__ = 'Pessoas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Nomes = Column(String(60), nullable=False)
    Idades = Column(Integer)


# criar as tabelas dos objetos criados
Base.metadata.create_all(engine)
# criar a sessão e linkar com o engine
Session = sessionmaker(bind=engine)
session = Session()



def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    if nome and idade:
        pessoa = Cadastro(Nomes=nome, Idades=idade)
        session.add(pessoa)
        session.commit()
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
        entry_nome.delete(0, END)
        entry_idade.delete(0, END)
        popula_lista()


def atualizar():
    selecao = listbox.curselection()
    if selecao:
        indice = selecao[0]
        id = int(listbox.get(indice).split(" - ")[0])
        nome = entry_nome.get()
        idade = entry_idade.get()
        if nome and idade:
            pessoa = session.query(Cadastro).filter_by(id=id).first()
            pessoa.Nomes = nome
            pessoa.Idades = idade
            session.commit()
            messagebox.showinfo("Atualização", "Atualização realizada com sucesso!")
            entry_nome.delete(0, END)
            entry_idade.delete(0, END)
            popula_lista()


def excluir():
    selecao = listbox.curselection()
    if selecao:
        indice = selecao[0]
        id = int(listbox.get(indice).split(" - ")[0])
        pessoa = session.query(Cadastro).filter_by(id=id).first()
        session.delete(pessoa)
        session.commit()
        messagebox.showinfo("Exclusão", "Exclusão realizada com sucesso!")
        popula_lista()


def popula_lista():
    listbox.delete(0, END)
    pessoas = session.query(Cadastro).all()
    for pessoa in pessoas:
        listbox.insert(END, f'{pessoa.id} - {pessoa.Nomes} - {pessoa.Idades}')


def explicar_crud():
    msg = "Bem-vindo ao sistema de cadastro de pessoas!\n\n" \
          "A lista exibe todas as pessoas cadastradas no sistema.\n\n" \
          "Para cadastrar uma nova pessoa, preencha o nome e a idade nos campos acima e clique em 'Cadastrar'.\n\n" \
          "Para atualizar uma pessoa existente, selecione o nome da pessoa na lista, edite os campos de nome e idade e clique em 'Atualizar'.\n\n" \
          "Para excluir uma pessoa, selecione o nome da pessoa na lista e clique em 'Excluir'.\n\n" \

    messagebox.showinfo("Sobre o CRUD", msg)

root = Tk()
root.title("Cadastro de Pessoas")

menubar = Menu(root)
menu_sobre = Menu(menubar, tearoff=0)
menu_sobre.add_command(label="Explicação", command=explicar_crud)
menubar.add_cascade(label="Sobre o CRUD", menu=menu_sobre)
root.config(menu=menubar)

label_nome = Label(root, text="Nome")
label_nome.grid(row=0, column=0)

entry_nome = Entry(root, width=30)
entry_nome.grid(row=0, column=1)

label_idade = Label(root, text="Idade")
label_idade.grid(row=1, column=0)

entry_idade = Entry(root, width=30)
entry_idade.grid(row=1, column=1)

botão_cadastrar = Button(root, text="Cadastrar", command=cadastrar)
botão_cadastrar.config(background='#00FA9A')
botão_cadastrar.grid(row=2, column=0)

button_atualizar = Button(root, text="Atualizar", command=atualizar)
button_atualizar.config(background='#A9A9A9')
button_atualizar.grid(row=2, column=1)

botão_excluir = Button(root, text="Excluir", command=excluir)
botão_excluir.config(background='#FF0000')
botão_excluir.grid(row=2, column=2)

listbox = Listbox(root, height=10, width=50)
listbox.grid(row=3, column=0, columnspan=3)


popula_lista()
root.mainloop()
