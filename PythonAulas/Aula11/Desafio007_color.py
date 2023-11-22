#Crie um programa que leia duas notas de um aluno e calcule sua média
n1 = float(input('Valor da prova 01: '))
n2 = float(input('Valor da prova 02: '))
m = (n1 + n2) / 2
print('A média das notas das provas é de \033[4;30;46m{:.1f}\033[m! Parabéns :)'.format(m))