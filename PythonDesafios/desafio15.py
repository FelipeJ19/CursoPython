dias = int(input('Quantos dias foi alugado: '))
km = float(input('Quantos km foram percoridos: '))
valor = (dias * 60) + (km * 0.15)
print('Total a pagar: R${:.2f}'.format(valor))