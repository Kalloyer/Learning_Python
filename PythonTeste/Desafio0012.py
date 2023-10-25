#Faça um programa que leia um preço de um produto e aplica 5% de desconto
n = int(input('Valor do produto: '))
d = n - (n * (5 / 100))
print('Valor do produto com 5% de desconto é de R$ {:.2f}'.format(d))