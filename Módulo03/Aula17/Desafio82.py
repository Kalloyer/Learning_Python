# Crie um programa que leia vários números, depois crie duas listas, uma com números pares e outra com ímpares
numero = list()
pares = list()
impares = list()
while True:
    numero.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N]: ")).lower().split()[0]
    if resposta == "n":
        break
for posicao, valores in enumerate(numero):
    if valores % 2 == 0:
        pares.append(valores)
    elif valores % 2 == 1:
        impares.append(valores)

print("===" * 15)
print(f"A lista completa é {numero}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
