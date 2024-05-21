# Crie uma matriz de dimensão 3x3 e mostre a mesma
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite um valor para [{linha}, {coluna}]: ")
        )
print(50 * "=")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^6}]", end="")
    print()
