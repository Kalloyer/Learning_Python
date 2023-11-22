# Crie um programa que leia um numero real e mostre na tela sua porção inteira
from math import trunc
numre = float(input('Digite um número: '))
#numint = (trunc(numre))
#print('O número real digitado é {} e sua porção inteira é {}!'.format(numre, numint))
#print('O número real digitado é {} e sua porção inteira é {}!'.format(numre, trunc(numre)))
print('O número real digitado é {} e sua porção inteira é {}!'.format(numre, int(numre)))