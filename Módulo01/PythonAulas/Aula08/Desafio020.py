#O mesmo professor quer sortear a ordem de apresentação do trabalho dos alunos
from random import shuffle
al1 = str(input('Primeiro aluno(a): '))
al2 = str(input('Segundo aluno(a): '))
al3 = str(input('Terceiro aluno(a):'))
al4 = str(input('Quarto aluno(a)'))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação dos alunos será {}'.format(lista))