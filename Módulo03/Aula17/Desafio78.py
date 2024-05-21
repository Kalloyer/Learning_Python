# Leia 5 valores numéricos e guarde-os em uma lista, mostre o maior e menor valr e sua posição
valores = []
maior = 0
menor = 0
for contagem in range(0, 5):
    valores.append(int(input(f"Digite o valor para a posição {contagem}: ")))
    if contagem == 0:
        maior = menor = valores[contagem]
    else:
        if valores[contagem] > maior:
            maior = valores[contagem]
        elif valores[contagem] < menor:
            menor = valores[contagem]
    contagem += 1
print(f"Você digitou os valores: {valores}.")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for listagem, valor in enumerate(valores):
    if valor == maior:
        print(f"{listagem}", end="...")
print()
print(f"O menor valor digitado foi {menor} nas posições: ", end="")
for listagem, valor in enumerate(valores):
    if valor == menor:
        print(f"{listagem}", end="...")
print()
