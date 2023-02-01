import ex2

op = 0
while op > 0:
    nome_fruta = input('digite o nome da fruta: ')
    cor_fruta = input('digite a cor da fruta: ')
    fruta = Fruta(nome=nome_fruta, cor=cor_fruta)

    op = int(input('deseja continuar [0] para sim:\n [1] para parar: '))
session.add(fruta)
session.commit()