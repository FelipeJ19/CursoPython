nome = str(input('Qual seu nome: ')).lower().strip()
#print('Seu nome tem Silva ? \n{}'.format('silva' in nome))

if(nome.count('silva')):
    print('Seu nome possui Silva')
else:
    print('Seu nome não possui Silva')
