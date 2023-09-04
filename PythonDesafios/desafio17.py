from math import sqrt, pow
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt(pow(co,2) + pow(ca, 2))

print('A hipotenusa vai medir: {:.2f}'.format(h))