nome = str(input('Qual é seu nome ? \n')).lower()

if nome == 'felipe':
    print('Que nome lindo você tem !')
else:
    print('Seu nome é tão normal !')
print('Bom dia, {} !'.format(nome.capitalize()))
