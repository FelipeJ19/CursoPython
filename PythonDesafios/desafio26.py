frase = str(input('Digite uma frase: ')).lower()

print('A frase possui {} letras "a"'.format(frase.count('a')))
print('O primeiro "a" esta na posição: {} '.format(frase.find('a')))
print('O ultimo "a" esta na posição: {}'.format(frase.rfind('a')))
