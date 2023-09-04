n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
print('Sua média é {:.2f}'.format(media))
if media >= 7.0:
    print('Você está Aprovado !')
elif media < 5.0:
    print('Você está Reprovado !')
else:
    print('Você está de Recuperação !')