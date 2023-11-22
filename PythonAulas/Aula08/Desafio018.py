# Faça um programa que leia o ângulo e mostre o seno, cosseno e tangente
#import math
#ang = int(input('Digite o ângulo: '))
#rad = math.radians(ang)
#seno = math.sin(rad)
#coss = math.cos(rad)
#tang = math.tan(rad)
#print('O valor digitado do ângulo é de {}!'.format(ang))
#print('=' * 40)
#print('O valor de seno é {:.2f}!\nO valor do cosseno é de {:.2f}!\nO valor de tangente é de {:.2f}!'.format(seno, coss, tang))

from math import radians, sin, cos, tan
ângulo = int(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O valor de seno do ângulo é {:.2f}, o de cosseno é {:.2f} e a tangente é {:.2f}!!!'.format(seno, cosseno, tangente))