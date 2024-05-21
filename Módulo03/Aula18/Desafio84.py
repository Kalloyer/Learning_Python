# Leia o nome e peso de várias pessoas e coloque em um lista, mostre quantas pessoas foram cadastradas, as pessoas mais leves e as mais pesadas
lista = []
cadastros = []
maior = menor = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(cadastros) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        elif lista[1] < menor:
            menor = lista[1]
    cadastros.append(lista[:])
    lista.clear()
    resposta = str(input("Quer continuar? [S/N]: ")).strip().lower()[0]
    if resposta == "n":
        break
print(30 * "==")
print(f"Os dados cadastrados foram {cadastros}.")
print(f"Ao todo foram cadastrados {len(cadastros)} pessoas.")
print(f"O maior peso cadastrado foi {maior}.", end=" ")
for pessoa in cadastros:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end=" ")
print()
print(f"O menor peso cadastrado foi {menor}.", end=" ")
for pessoa in cadastros:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end=" ")
print()
