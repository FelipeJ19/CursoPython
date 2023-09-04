vel = int(input('Qual a velocidade ? \n'))
multa = (vel - 80) * 7

if(vel > 80):
    print('Voce foi multado em R${:.2f} !'.format(multa))
else:
    print('Você está na velocidade permitida !')

