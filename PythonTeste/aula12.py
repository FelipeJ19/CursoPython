nome = str(input('Qual é seu nome ? \n')).lower()

if nome == 'felipe':
    print('Que nome lindo você tem !')
elif nome in 'ana maria paula jessica ':
    print('Que belo nome femenino !')
else:
    print('Seu nome é tão normal !')
print('Bom dia, {} !'.format(nome.capitalize()))
