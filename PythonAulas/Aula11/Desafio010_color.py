#Mostro um progrma que leia quanto dinheiro a pessoa tem e mostre quantos dólares da 4,99 o dolar
n = float(input('Saldo atual: R$ '))
d = n / 4.99
print('Você consegue comprar \033[1;32mUS$ {:.2f}\033[m dólares!'.format(d))