#tempo = int(input('Quanto anos tem seu carro: '))
#if tempo <= 5:
#    print('Seu carro é novo')
#else:
#    print('Seu carro é velho')
#print('Seu carro é novo' if tempo <= 5 else 'Seu carro é velho')
#print('*' * 10, 'FIM', '*' * 10)
####################################################################
#nome = str(input('Qual é o seu nome? '))
#if nome == 'Kalleu':
#    print('Muito loco seu nome!')
#else:
#    print('Que nome de normal...')
#print('Prazer em te conhecer {}!!!'.format(nome))
####################################################################
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 70:
    print('Você está acima da média, sua note é {:.1f}, Parabéns!!!'.format(m))
else:
    print('Infelizmenteo você ficou abaixo da média {:.1f}, estude mais na próxima.'.format(m))