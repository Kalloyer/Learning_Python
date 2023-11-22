# Leia a velocidade do carro e acima do 80km/h multa de R$7,00 por km acima do limite
velocidade = float(input('Digite a velocidade do veículo em Km: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R$ {:.2f}, pois ultrapassou o limite da pista!'.format(multa))
print('Você está dentro do limite de velocidade, parabéns!')