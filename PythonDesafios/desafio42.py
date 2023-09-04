a = float(input('Digite a primeira reta:'))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if (a < b + c) and (b < c + a) and (c < a + b):
    print('é um triangulo ', end='')

    if a == b == c:
        print('equilátero !')

    elif (a == b != c) or (a == c != b) or (c == b != a):
        print('isóceles !')

    elif a != b != c != a:
        print('escaleno !')

else:
    print('Não é um triangulo')
