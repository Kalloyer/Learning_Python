# Gere 5 números aleatórios e mostre a lista gerada o menor e o maior valor entre eles
from random import randint

numero = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
print("Os números gerados foram: ", end="")
for contagem in numero:
    print(contagem, end=" ")
print(f"\nO maior número da lista é {max(numero)} e o menor é {min(numero)}.")
