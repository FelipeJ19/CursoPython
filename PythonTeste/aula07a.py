n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('O valor da soma é {}\nO valor da mutiplicação é {}\nO valor da divisão é {:.3f}\nO valor da divisão inteira é {}\nO valor da exponenciação é {}'.format(s, m, d, di, e))