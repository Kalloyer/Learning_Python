# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quant dias alugado: '))
km = float(input('Quantos KM rodados: '))
total = (dias * 60) + (km * 0.15)
print('\033[4;32;45m O total a pagar é de R${:.2f}\033[m'.format(total))