# Escreva um programa que leia o valor em metro e converta em contimetro e milimetros (colocar km, hectometro, decametros, decimetros)
n = float(input('Qual o valor em metros? '))
dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10
print('A medida {}m corresponde a \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm \n{}km \n{}hm \n{}dam'.format(n, dm, cm, mm, km, hm, dam))