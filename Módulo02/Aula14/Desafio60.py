# leia um numero que fale o seu fatorial (utilizar o for e o while)
from time import sleep

valor = int(input("Digite um número: "))
número = valor
fatorial = 1
print("Calculando o fatorial do número digitado...")
sleep(3)
print("{}! = ".format(valor), end="")
while número > 0:
    print("{}".format(número), end="")
    print(" x " if número > 1 else " = ", end="")
    fatorial *= número
    número -= 1
print(fatorial)

# Feito utilizando o for:
"""c = 0
print("{}! = ".format(valor), end="")
for c in range(1, número):
    print("{}".format(número), end="")
    print(" x " if c < número + 1 else " = ", end="")
    fatorial *= número
    número -= 1
print(fatorial)"""
