# 4 jogadores jogam um dado e tenham resultado aleatórios, coloquem em ordem sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter

maior = 0
jogadores = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6),
}
ordemjogador = {}

for chave, valor in jogadores.items():
    print(f"{chave} tirou o valor {valor} no dado.")
    sleep(1)
print(35 * "=")
ordemjogador = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f"{"Ranking dos Jogaodres":^35}")
print(35 * "=")
for indice, valor in enumerate(ordemjogador):
    print(f"{indice +1}º lugar: {valor[0]} com {valor[1]} pontos!")
    sleep(1)
