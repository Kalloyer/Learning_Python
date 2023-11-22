#Faça um programa que leia a altura e a largura de uma parede e calcule a área e a quantidade de tinta necessária, sabendo que cada litro de tinta pinta 2m2
lgr = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = lgr * alt
tinta = area / 2
print('A área de sua parede é de {}m² \nA quantidade necessária de tinta para pintar sua parede são {}l'.format(area, tinta))