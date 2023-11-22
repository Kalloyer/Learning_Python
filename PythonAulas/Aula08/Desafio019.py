#Faça um programa que sorteia um aluno para apagar o quadro
import random
al1 = str(input('Nome do aluno(a): '))
al2 = str(input('Nome do aluno(a): '))
al3 = str(input('Nome do aluno(a): '))
al4 = str(input('Nome do aluno(a): '))
alunos = random.choice([al1, al2, al3, al4])
print('=' * 50)
print('O aluno sorteado para apagar o quadro é {}!'.format(alunos))