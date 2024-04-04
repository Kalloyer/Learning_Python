# Programa pergunta o valor da casa, salário e tempo que ele irá pagar | calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
tempo = float(input('Qunato tempo você irá pagar? (anos) '))
prestacao = casa / (tempo * 12)
if (salario * 0.3) >= prestacao:
    print('Seu empréstimo foi aprovado! \nVocê irá pagar {:.2f} ao mês.'.format(prestacao))
else :
    print('Seu empréstimo foi recusado, pois estrapola 30% de seu salário.')