# Calcule a soma de todos os números impares, que são mutiplos de três entre 1 a 500
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print(
    "A soma de todos os valores ({}), divisiveis por três é de {}!".format(
        contador, soma
    )
)
