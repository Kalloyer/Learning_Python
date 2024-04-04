# Leia seis números inteiros e mostre a penas a soma daqueles que forem pares
soma = 0
for c in range(1, 7):
    numero = int(input("Digite o {} valor: ".format(c)))
    if numero % 2 == 0:
        soma += numero
print("A soma dos números pares digitados é de {}!".format(soma))
