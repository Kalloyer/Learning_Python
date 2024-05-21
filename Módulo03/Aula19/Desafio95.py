# Aprimore o desafio93, leia varios jogadores e de uma vizualização detalhada de cada jogador
dados = {}
totalpartidas = []
time = []
while True:
    dados.clear()
    dados["Nome"] = str(input("Nome: "))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    totalpartidas.clear()
    for contador in range(1, partidas + 1):
        totalpartidas.append(int(input(f"Quantos gols na partida {contador}? ")))
    dados["Gols"] = totalpartidas[:]
    dados["Total"] = sum(totalpartidas)
    time.append(dados.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
        if resposta in "sn":
            break
        print("*ERRO* Digitar apenas S ou N.")
    if resposta == "n":
        break
print(40 * "=")
print("Cod", end="")
for indice in dados.keys():
    print(f"{indice:<15}", end="")
print()
print(40 * "=")
for chave, valor in enumerate(time):
    print(f"{chave:>3}", end="")
    for dado in valor.values():
        print(f"{str(dado):<15}", end="")
    print()
print(40 * "=")
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para o programa): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"*ERRO* Não existe jogador com o código {busca}.")
    else:
        print(f'== Levantamento de Jogador == {time[busca]["Nome"]}: ')
        for indice, gol in enumerate(time[busca]["Gols"]):
            print(f"=> No jogo {indice + 1} fez {gol} gols.")
    print(40 * "=")
print(f'{" VOLTE SEMPRE ":=^40}')
