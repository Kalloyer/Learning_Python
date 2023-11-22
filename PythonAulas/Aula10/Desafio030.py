#faça um programa que leia o numero inteiro e mostre se ele é par ou impar
numero = int(input('Digite um número: '))
print('O número {} é par'.format(numero) if numero % 2 == 0 else 'O número {} é impar'.format(numero))