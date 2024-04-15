# Leia vários números, no final mostra a média entre eles, o menor e maior número, pergunte ao usuário se quer ou não continuar
número = contagem = média = soma = maior = menor = 0
continuar = "s"
while continuar in "Ss":
    número = int(input("Digite um número: "))
    soma += número
    contagem += 1
    if contagem == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número
    continuar = str(input("Quer continuar, [S/N]: ")).lower().strip()[0]
print(25 * "==")
média = soma / contagem
print(
    "Foram digitados {} números.\nA média dos valores digitados é de {:.2f}.".format(
        contagem, média
    )
)
print("O maior número digitado foi {} e o menor foi {}!".format(maior, menor))
print("Finalizado")
