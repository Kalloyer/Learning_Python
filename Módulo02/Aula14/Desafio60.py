# leia um numero que fale o seu fatorial (utilizar o for e o while)
from time import sleep

valor = int(input("Digite um número: "))
número = valor
fatorial = 1
print("Calculando o fatorial do número digitado...")
sleep(3)
while número > 0:
    print("{} x ".format(número), end="")
    print(" x " if número > 1 else " = ", end="")
    fatorial *= número
    número -= 1
print(fatorial)
