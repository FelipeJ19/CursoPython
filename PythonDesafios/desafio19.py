import random

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
alunos = [a1, a2, a3, a4]
s = random.choice(alunos)

print('O aluno escolhido foi: {} '.format(s))