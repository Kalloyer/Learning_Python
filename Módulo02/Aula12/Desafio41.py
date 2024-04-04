#Leia a data de nascimento e mostre a categoria do atleta de natação
from datetime import date
atual = date.today().year
data = int(input('Digite o seu ano de nascimento: '))
ano = atual - data
if ano <= 9:
    print('Sua categoria é Mirim')
elif ano <= 14:
    print('Sua categoria é Infantil')
elif ano <= 19:
    print('Sua categoria é Junior')
elif ano <= 20:
    print('Sua categoria é Sênior')
else:
    print ('Sua categoria é Master')