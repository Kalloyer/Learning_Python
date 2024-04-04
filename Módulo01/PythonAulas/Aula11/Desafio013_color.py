#Faça um programa que leia o salário e de um aumento de 15%
salario = int(input('Digite seu salário: R$'))
aumento = salario + (salario * (15 / 100))
print('\033[30;43mCom o aumento você passa a receber\033[m \033[1;30;42mR${:.2f}\033[m'.format(aumento))