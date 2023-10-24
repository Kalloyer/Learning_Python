#Crie um programa que leia seu número e mostre o dobro, tripo e raiz quadrada
n1 = int(input('Digite um valor:'))
d = n1 * 2
t = n1 * 3
r = n1 / 2
print('O dobro do valor é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(d, t, r))