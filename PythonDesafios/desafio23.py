num = int(input('Digite um numero: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('A milhar é: ', m)
print('A centena é: ', c)
print('A dezena é: ', d)
print('A unidade é: ', u)
