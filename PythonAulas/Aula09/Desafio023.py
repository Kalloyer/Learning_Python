#Faça um programa que leia o numero 0 a 9999 e mostre cada um dos digitos separados
numero = int(input('Digite um número: '))
#numero.split()
#unidade = numero[3]
#centena = numero[2]
#dezena = numero[1]
#milhar = numero[0]
#int('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, centena, dezena, milhar))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número inserido {}.\n'
      'Sua unidade é {}\n'
      'Sua dezena é {}\n'
      'Sua centena é {}\n'
      'Seu milhar é {}'
      .format(numero, u, d, c, m))