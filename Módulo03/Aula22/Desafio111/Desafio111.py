# Crie pacote chamado de UtilidadeCeV com dois módulo Moeda e Dado e importe os dados solicitados
from UtilidadesCeV import Moeda

p = float(input("Digite o preço R$ "))
Moeda.resumo(p, 80, 20)
