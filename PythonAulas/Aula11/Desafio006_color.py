#Crie um programa que leia seu número e mostre o dobro, tripo e raiz quadrada
n1 = int(input('Digite um valor:'))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
#print('O dobro do valor é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(d, t, r))
cores = {'limpa': '\033[m',
         'RoxoNegr': '\033[1;35m',
         'BrancoAzul': '\033[30;46m',
         'CinzaBranco': '\033[37;40m'}
print('O dobro do valor é {}{}{}. \nO triplo é {}{}{}. \nE a raiz quadrada é {}{:.2f}{}.'
      .format(cores['RoxoNegr'], (n1 * 2), cores['limpa'], cores['CinzaBranco'], (n1 * 3), cores['limpa'], cores['BrancoAzul'], pow(n1 , (1/2)), cores['limpa']))