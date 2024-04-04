# Escreva um programa que leia o valor em metro e converta em contimetro e milimetros (colocar km, hectometro, decametros, decimetros)
n = float(input('Qual o valor em metros? '))
dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10
cores = {'Limpa': '\033[m',
         'Vermelho': '\033[1;31m',
         'Verde': '\033[1;32m',
         'Amarelo': '\033[1:33m',
         'Azul': '\033[1;34m',
         'Roxo': '\033[1;35m',
         'AzulClaro': '\033[1;36m'}
print('A medida {}m corresponde a \n{}{:.0f}{}dm \n{}{:.0f}{}cm \n{}{:.0f}{}mm \n{}{}{}km \n{}{}{}hm \n{}{}{}dam'
      .format(n,
              cores['Vermelho'], dm, cores['Limpa'],
              cores['Verde'], cm, cores['Limpa'],
              cores['Amarelo'], mm, cores['Limpa'],
              cores['Azul'], km, cores['Limpa'],
              cores['Roxo'], hm, cores['Limpa'],
              cores['AzulClaro'], dam, cores['Limpa']))
