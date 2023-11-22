# Leia o nome da pessoa e separa o primeiro e ultimo nome
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}.\n'
      'Seu último nome é {}.'
      .format(nome[0], nome[len(nome) - 1]))
