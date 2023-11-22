#Faça um programa que leia um preço de um produto e aplica 5% de desconto
valor = int(input('Valor do produto: R$'))
desc = valor - (valor * (5 / 100))
print('O valor do produto com 5% de desconto é de R${:.2f}'.format(desc))