# Faça um programa que leia um número interio e mostro seu sucessor e antecessor
n1 = int(input('Dígite um valor: '))
s = n1 + 1
a = n1 - 1
cores = {'limpa': '\033[m',
         'VermelhoeAmarelo': '\033[31;42m',
         'AzulNegrito': '\033[1;36m',
         'RoxoUnderline': '\033[4;35m',
         'VerdeBack': '\033[42m'}
print('Valor digitado: {}{}{}. \nSeu sucessor: {}{}{}. \nSeu antecessor: {}{}{}.'
      .format(cores['VermelhoeAmarelo'], n1, cores['limpa'], cores['AzulNegrito'], s, cores['limpa'], cores['RoxoUnderline'], a, cores['limpa']))

# print('Valor digitado: {} \nSeu sucessor: {} \nSeu antecessor: {}'.format(n1, (n1 + 1), (n1 - 1)))
