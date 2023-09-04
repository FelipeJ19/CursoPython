km = int(input('Qual a distancia da sua viajem ? \n'))
v1 = km * 0.50
v2 = km * 0.45

if(km <= 200):
    print('O valor da passagem é R${:.2f}'.format(v1))
else:
    print('O valor da passagem é {:.2f}'.format(v2))
