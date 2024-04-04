#Faça um programa que leia o salário e de um aumento de 15%
salario = int(input('Digite seu salário: R$'))
aumento = salario + (salario * (15 / 100))
print('Com o aumento você passa a receber R${:.2f}'.format(aumento))