# Faça uma Mega Sena, pergunte quantos jogos serão, e cada jogo terá 6 números entre 1 e 60
from random import randint
from time import sleep

contagem = 0
mega = []
lista = []
total = 1

print(45 * "=")
print(f'{"MEGA DA VIRADA":^45}')
print(45 * "=")
jogos = int(input("Quantos jogos você deseja que eu sorteie? "))
while total <= jogos:
    contagem = 0
    while True:
        numero = randint(1, 60)
        if numero not in mega:
            mega.append(numero)
            contagem += 1
        if contagem >= 6:
            break
    mega.sort()
    lista.append(mega[:])
    mega.clear()
    total += 1
print(13 * "=", f"Sorteando {jogos} Jogos", 13 * "=")
for indice, listagem in enumerate(lista):
    print(f"Jogo {indice + 1}: {sorted(listagem)}.")
    sleep(1)
print(f'{' Boa sorte! ':=^45}')
