# Leia três número e mostre qual é o maior e qual é o menor
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor digitado é {}!\n'
      'O menor valor digitado é {}!'.format(maior, menor))
# if lista >
# print('O maior número digitado é {}!'.format())
# print('O maior número digitado é {}!'.format(max(a, b, c)), '\nO menor número digitado é {}!'.format(min(a, b, c)))
