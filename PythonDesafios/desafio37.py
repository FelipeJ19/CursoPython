numero = int(input('Qual o numero que deseja converter ?\n'))
escolha = int(input('escolha a conversão\n1 = binario\n2 = octal\n3 = hexadecimal\n'))

if escolha == 1 :
    print('O valor {} em binario é: {} '.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O valor {} em octal é: {} '.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O valor {} em hexadecimal é: {} '.format(numero, hex(numero)[2:]))
else:
    print('Opcão invalida !')
