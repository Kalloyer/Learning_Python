#Fazer programa que converta ⁰C em ⁰F
C = float(input('Informe a temperatura em Celsius: '))
F = (C * 9/5) + 32
print('A temperatura de \033[1;31m{}⁰C\033[m corresponde a \033[1;31m{}⁰F\033[m.'.format(C, F))