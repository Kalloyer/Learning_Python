#Leia a data de nasc e informe se ainda vai se alistar, tem que se alistar, já passou do tempo de se alistar | Mostre também quanto tempo falta para se alistar
#nasc = int(input('Digite o ano que nasceu: '))
#ano = 18 - (2024 - nasc)
#if nasc > 2006:
#    print('Ainda não é necessário realizar o alistamento. \nMas faltam apenas {} anos para se alistar.'.format(ano))
#elif nasc == 2006:
#    print('Está na hora de se alistar, acesse o site do exército e faça seu cadastro!')
#else:
#    print('Já passou do tempo de se alistar, passou tem {} anos.'.format((2024 - nasc) - 18))

from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    print('Você ainda vai ter que se alistar no exército, daqui a {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar imediatamente!!!')
else:
    print('Você já passou do tempo de se alistar, já se passaram {} anos do alistamento!'.format(idade - 18))