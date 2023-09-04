salario = float(input('Qual seu salario ?\n'))
a1 = salario * 10 / 100
a2 = salario * 15 / 100

if salario > 1250:
    print('Seu aumento foi de R${:.2f}\nSeu salario atual é de R${:.2f}'.format(a1, salario + a1))
else:
    print('Seu aumento foi de R${:.2f}\nSeu salario atual é de R${:.2f}'.format(a2, salario + a2))
