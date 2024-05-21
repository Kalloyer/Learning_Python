# Tupla de 0 a 20 e peça para digitar um valor entre 0 e 20 escrevendo-o por extenso.
contagem = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    valor = int(input("Digite um valor entre 0 e 20: "))
    if valor < 0 or valor > 20:
        print("Tente novamente...", end=" ")
    else:
        print(f"Você digitou o número {contagem[valor]}!")
    continuar = " "
    while continuar not in "sn":
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
    if continuar == "n":
        break
print(30 * "=")
print("Fim do Programa")
