#leia tres retas e mostre se ela pode formar um triangulo
print('*' * 10, 'Formardor de Triângulos', '*' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo')