#Pergunte a distancia em Km e calcule o preço da passagem de 0,50 por KM até 200Km e acima disso é 0,45
distancia = float(input('Qual a distância da viajem em Km: '))
if distancia <= 200:
    print('O valor da sua passagem é de R$ {:.2f}'.format(distancia * 0.5))
else:
    print('O valor da sua passagem é de {:.2f}'.format(distancia * 0.45))