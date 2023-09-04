valor = float(input('Qual o valor da casa ?\n'))
salario = float(input('Qual o seu salario ?\n'))
anos = int(input('Quantos anos você vai pagar ?\n')) * 12
s = salario * 30 / 100

if valor / anos > s:
    print('Seu emprestimo foi Negado !')
else:
    print('Seu emprestimo foi Aprovado !')
