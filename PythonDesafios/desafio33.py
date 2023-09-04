n1 = int(input('Digite um numero: \n'))
n2 = int(input('Digite um numero: \n'))
n3 = int(input('Digite um numero: \n'))
if(n1 < n2) and (n1 < n3):
    menor = n1
if(n2 < n1) and (n2 < n3):
    menor = n2
if(n3 < n2) and (n3 < n1):
    menor = n3
if(n3 > n2) and (n3 > n1):
    maior = n3
if(n2 > n3) and (n2 > n1):
    maior = n2
if(n1 > n2) and (n1 > n3):
    maior = n1

print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))
