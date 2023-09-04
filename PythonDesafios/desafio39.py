from datetime import date
ano = int(input('Qual seu ano de nascimento ?\n'))
idade = date.today().year - ano

if idade == 18:
    print('Você deve se alistar !')
elif idade < 18:
    print('Faltam {} anos para o seu alistamento !'.format(18 - idade))
else:
    print('Você deveria ter se alistado a {} anos !'.format(idade - 18))
