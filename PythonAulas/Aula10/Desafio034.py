#leia o salario e acima de R$ 1302 tem aumento de 10% e abaixo disso tem aumento de 15%
salario = float(input('Digite o valor do seu salário: '))
if salario >= 1302.00:
    print('Você receberá um aumento de 10% e o seu salário de {} vai para {:.2f}!'.format(salario, salario + (salario * 0.1)))
else:
    print('Você receberá um aumento de 15% e o seu salário de {} vai para {:.2f}!'.format(salario, salario + (salario * 0.15)))