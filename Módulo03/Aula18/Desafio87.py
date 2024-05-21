# Use o desafio anterior e mostra a soma dos valores pares, a soma dos valores da terceira coluna e o maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = somac = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite uma valor para [{linha}, {coluna}]: ")
        )
print(50 * "=")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            somap += matriz[linha][coluna]
    print()
print(50 * "=")
print(f"A soma dos valores é de: {somap}.")
for linha in range(0, 3):
    somac += matriz[linha][2]
print(f"A soma dos valores da terceira coluna é de {somac}.")
if coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
    print(f"O maior valor da segunda linha é {maior}.")
