# Digite 7 valores numéricos, cadastreos em uma única lista, separes os valores impares e pares nor final mostre os em ordem crescente
lista = [[], []]
numero = 0
for contagem in range(0, 7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    elif numero % 3 == 0:
        lista[1].append(numero)
print(60 * "=")
print(f"Esses foram os números pares cadastrados: {sorted(lista[0])}.")
print(f"Esses foram os números ímpares cadastrados: {sorted(lista[1])}.")
