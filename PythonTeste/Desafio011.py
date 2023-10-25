#Faça um programa que leia a altura e a largura de uma parede e calcule a área e a quantidade de tinta necessária, sabendo que cada litro de tinta pinta 2m2
l =int(input('Qual a largura da parede: '))
a = int(input('Qual a altura da parede: '))
s = l * a
t = s // 2
print('A área de sua parede é de {} metros \nA quantidade necessária de tinta para pintar sua parede é de {} litros'.format(s, t))