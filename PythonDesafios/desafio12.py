preco = float(input('Digite um valor: '))
desconto = preco * 0.05
vf = preco - desconto
print('Valor produto: {:.2f}R$\nValor desconto: {:.2f}R$\nValor final: {:.2f}R$'.format(preco, desconto, vf))