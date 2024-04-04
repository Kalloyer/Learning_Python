"""r = "S"
while r == "S":
    numero = int(input("Digite um valor: "))
    r = str(input("Quer continuar [S/N] ").upper())
print("FIM")"""

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} ímpares".format(par, impar))
