# Faça um programa que jogue par ou impar, o jogo será interrompido quando o jogador perder
from random import randint
from time import sleep

vitória = 0
print(20 * "~~")
print("        Vamos jogar PAR ou ÍMPAR")
print(20 * "~~")
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 10)
    soma = jogador + computador
    opcao = " "
    while opcao not in "pi":
        opcao = str(input("Par ou Ímpar? [P/I]: ")).lower().strip()[0]
    print(
        f"Você jogou {jogador} e o computador {computador}, o total foi de {soma}!",
        end=" -> ",
    )
    print("Deu PAR" if soma % 2 == 0 else "Deu ÍMPAR")
    if opcao == "p":
        if soma % 2 == 0:
            print("Você VENCEU!!!")
            vitória += 1
        else:
            print("Você PERDEU!")
            break
    elif opcao == "i":
        if soma % 2 == 1:
            print("Você VENCEU!!!")
            vitória += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
    sleep(2)
    print(30 * "-")
print(20 * "-F-")
print(f"GAME OVER, mas venceu {vitória} vezes!")
