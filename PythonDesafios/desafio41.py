from datetime import date
ano = int(input('Qual sua ano de nascimento ?\n'))
idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua  categoria é INFATNTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
