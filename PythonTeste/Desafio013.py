#Faça um programa que leia o salário e de um aumento de 15%
s = int(input('Digite seu salário: '))
a = s + (s * (15 / 100))
print('Com o aumento você passa a receber R$ {:.2f}'.format(a))