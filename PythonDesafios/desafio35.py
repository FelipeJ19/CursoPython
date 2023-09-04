n1 = int(input('Digite a primeira reta: \n'))
n2 = int(input('Digite a segunda reta: \n'))
n3 = int(input('Digite a terceira reta: \n'))

if(n1 < n2 + n3) and (n3 < n1 + n2) and (n2 < n3 + n1):
    print('As 3 retas podem formar um triangulo')
else:
    print('As três retas não podem formar um triangulo')

