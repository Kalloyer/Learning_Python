# Use o desafio 28 e mostre quantos palpites foram necessários para vencer
from random import randint

computador = randint(0, 10)
print(
    "Sou seu computador, estou processando um número entre 0 e 10, tente adivinhá-lo..."
)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Digite o seu palpite, entre 0 e 10: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Ta perto, tenta de novo.")
        elif jogador > computador:
            print("Menos... tenta de novo...")
print("Você acertou, mas fez {} palpites.".format(palpites))
