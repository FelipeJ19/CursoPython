import random
num = int(random.uniform(0, 5))
tentativa = int(input('Adivinhe o numero entre 0 e 5: \n'))

if(tentativa == num):
    print('Você acertou !')
else:
    print('Você errou !')
    print('O numero era {}'.format(num))

print('Obrigado por Jogar !')

# while(tentativa != num):
#     tentativa = int(input('Digite outro numero: \n'))
# else:
#     print('Você acertou, Parabens !')"""

