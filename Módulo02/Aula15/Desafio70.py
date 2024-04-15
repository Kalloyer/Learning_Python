# Leia o nome e preço de vários produtos, pergunte se irá parar ou continuar. Depois mostre o total gasto, produtos mais de R$ 1.000 e o nome do produto mais barato
soma = caro = menor = contagem = 0
maisbarato = ""
while True:
    print(30 * "=")
    print("    Loja do Jorgingameplys    ")
    print(30 * "=")
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço, R$"))
    soma += preco
    contagem += 1
    if preco >= 1000:
        caro += 1
    if contagem == 1 or preco < menor:
        menor = preco
        maisbarato = produto
    continuar = " "
    while continuar not in "sn":
        print(30 * "=")
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
    if continuar == "n":
        print("=====Programa Finalizado=====")
        break
print(f"O total gasto foi de R$ {soma:.2f}.")
print(f"Temos {caro} produtos, acima de R$ 1.000,00")
print(f"O produto mais barato foi {maisbarato} que custa R${menor:.2f}.")
