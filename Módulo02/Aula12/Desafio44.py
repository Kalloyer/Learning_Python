#Programa que calcule o valor pago por um produto com as consições de dinheito 10% de desconto | a vista cartão 5% | até em 2x preço normal | 3x ou mais 20% de juros
print('{:=^40}'.format('Lojinha'))
produto = float(input('Digite o valor do produto: R$ '))
print('''Escolha sua forma de pagamento:
      [1] Dinheiro
      [2] Cartão à vista
      [3] Parcelado em 2x
      [4] Parcelado em 3x ou mais''')
opcao = int(input('Escolha uma das formas acima: '))
if opcao == 1:
    print('Você ganhou um desconto, o produto irá sair por R${:.2f}!'.format(produto - (produto * 0.1)))
elif opcao == 2:
    print('Você ganhou um desconto, o produto irá sair por R${:.2f}'.format(produto - (produto * 0.05)))
elif opcao == 3:
    print('O produto irá sair por R${:.2f}, parcelado em 2x de R${:.2f} sem juros'.format(produto, produto / 2))
else:
    print('O produto irá sair por R${:.2f}, parcelado em 3x de R${:.2f} ou mais.'.format(produto + (produto * 0.2), (produto + (produto * 0.2)) / 3))

