ano = int(input('Qual o ano ? \n'))

if(ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('esse ano é Bissexto')
else:
    print('esse ano não é Bissexto')
