# Faça um programa que leia um número e mostre a tabuada
n = int(input('Digite um número: '))
# t = (n * 1, n * 2,n * 3,n * 4,n * 5,n * 6,n * 7,n * 8,n * 9,n * 10,)
# print('A tabuada do valor digitado é {}'.format(t))
cores = {'limpa': '\033[m',
         'Azul': '\033[1;36m',
         'Vermelho': '\033[1;31m',
         'Roxo': '\033[35m'}
print(cores['Roxo'], '-' * 15, cores['limpa'])
print('{} x{:2} = {}{}{}'.format(n, 1, cores['Azul'], n * 1, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 2, cores['Azul'], n * 2, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 3, cores['Azul'], n * 3, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 4, cores['Azul'], n * 4, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 5, cores['Azul'], n * 5, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 6, cores['Vermelho'], n * 6, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 7, cores['Vermelho'], n * 7, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 8, cores['Vermelho'], n * 8, cores['limpa']))
print('{} x{:2} = {}{}{}'.format(n, 9, cores['Vermelho'], n * 9, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 10, cores['Vermelho'], n * 10, cores['limpa']))
print(cores['Roxo'], '-' * 15, cores['limpa'])
