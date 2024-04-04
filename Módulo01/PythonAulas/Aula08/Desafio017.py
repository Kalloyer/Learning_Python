#Faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o comprimento da hipotenusa
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
#print('=' * 60, '\nO comprimento da Hipotenusa arredondado é de {}!'.format(ceil(hi)))
print('=' * 60, '\nO comprimento da Hipotenusa é de {:.2f}!'.format(hi))