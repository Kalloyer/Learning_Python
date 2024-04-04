# a = 3
# b = 5
# print('Os valores são \033[4;36m{}\033[m e \033[4;31m{}\033[m!'.format(a, b))
nome = 'Kalleu'
# print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[1;36m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'BrancoNegrito': '\033[7;30m',
         'AzulSub': '\033[4;34m',
         'VermelhoBack': '\033[41m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['AzulSub'], nome, cores['limpa']))
