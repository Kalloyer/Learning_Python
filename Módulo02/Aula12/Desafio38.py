#Leia doi números inteiros e mostre se o valor do primeiro é maior que o segundo, vice e versa e não existe valor maior
#num1 = int(input('Digite o primeiro número inteniro: '))
#num2 = int(input('Digíte o segundo número inteiro: '))
#if num1 > num2:
#    print('O primeiro número ({}) é maior que o segundo ({}).'.format(num1, num2))
#elif num2 > num1:
#    print('O segundo número ({}) é maior que o primeiro ({}).'.format(num2, num1))
#else:
#    print('Ambos os números {} e {} são iguais.'.format(num1, num2))

from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos hoje e em {}!'.format(nasc, idade, atual))