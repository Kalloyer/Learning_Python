#Note: Ordem de Procedência: 1 = () | 2 = ** | 3 = *;/;//;% | 4 = +;-
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
print('A soma do produto é {} \nA subtração é {}'.format(s, su))
print('A multiplicação é {} \nA divisão é {:.2f} \nE a divisão inteira é {}'.format(m, d,   di))