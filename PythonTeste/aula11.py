nome = 'Felipe'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto': '\033[7;30m'}

print('Olá, Muito prazer em te conhecer {}{}{} !!'.format(cores['azul'], nome, cores['limpa']))
