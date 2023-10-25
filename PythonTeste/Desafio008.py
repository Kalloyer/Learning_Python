# Escreva um programa que leia o valor em metro e converta em contimetro e milimetros
n = int(input('Qual o valor em metros? '))
c = n * 100
m = n * 1000
print('O valor em centimentros é {}cm e em militros é {}mm!'.format(c, m))