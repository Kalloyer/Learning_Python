# Leio o nome e partidas que um jogador jogou, quantidade de gols de cada partida, no final mostre no dicionário incluindo o total de gols
dados = {}
totalpartidas = []
dados["Nome"] = str(input("Nome: "))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for contador in range(1, partidas + 1):
    totalpartidas.append(int(input(f"Quantos gols na partida {contador}? ")))
dados["Gols"] = totalpartidas[:]
dados["Total"] = sum(totalpartidas)
print(40 * "=")
for chave, indice in dados.items():
    print(f"O campo {chave} tem o valor {indice}.")
print(40 * "=")
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for indice, valor in enumerate(dados["Gols"]):
    print(f"=> Na partida {indice + 1 }, fez {valor} gols.")
print(f'Foi um total de {dados["Total"]} gols.')
