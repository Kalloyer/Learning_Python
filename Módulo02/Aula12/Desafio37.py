#Programa que leia um numero inteiro e peça para escolher qual será a base de conversão: binário / octal / hexadecimal
num = int(input('Insira um número inteiro: '))
print('''Escolha umas das bases para conversão:
      [1] Converter para Binário
      [2] Converter para Octal
      [3] Converter para Hexadecimal''') 
opcao = int(input('Escolha uma das opções acima: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('A opção não existe!')