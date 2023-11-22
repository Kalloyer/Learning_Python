#Crie um programa que leia seu número e mostre o dobro, tripo e raiz quadrada
n1 = int(input('Digite um valor:'))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
#print('O dobro do valor é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(d, t, r))

print('O dobro do valor é {}. \nO triplo é {}. \nE a raiz quadrada é {:.2f}.'.format((n1 * 2), (n1 * 3), pow(n1 , (1/2))))