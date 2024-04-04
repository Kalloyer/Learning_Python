#Faça um programa que leia o nome completo de uma pessoae mostre, tudo maiusculo, minúsculo,
#quantas letras (sem espaço), quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculo: {} \nNome em minúsculo: {} \nQuantas letras tem seu nome: {}'
      '\nQuantas letras tem o primeiro nome: {}'
      .format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' ')))
