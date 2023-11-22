#Faça um programa que leia um preço de um produto e aplica 5% de desconto
valor = int(input('Valor do produto: R$'))
desc = valor - (valor * (5 / 100))
print('O valor do produto com \033[1;31m5%\033[m de desconto é de \033[4;32mR${:.2f}\033[m'.format(desc))