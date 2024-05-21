# Crie um programa que leia vários número e mostre, quantos números foram digitados, a lista em forma decrescente se o valor 5 foi ou não digitado
lista = []
num5 = list()
while True:
    lista.append(int(input("Digite um número: ")))
    respota = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if respota == "n":
        break
for posicao, valor in enumerate(lista):
    if valor == 5:
        num5.append(posicao)
print(f"Os valores digitados foram: {len(lista)}.")
lista.sort(reverse=True)
print(f"A lista em forma decrescente é {lista}.")
if 5 in lista:
    print(f"O número 5 se encontra na lista, na posição {num5}.")
else:
    print("O número 5 não foi digitado em nenhum momento.")
print("==" * 30)
print("Programa Finalizado")
