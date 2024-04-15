# Simule um caixa eletrônico e infome quantas cédulas de cada valor será entregue, cédulas de 50, 20, 10 e 1.
from time import sleep

print(40 * "=")
print("{:^40}".format("Banco do Iguin"))
print(40 * "=")
valor = int(input("Qual valor você quer sacar? R$"))
valortotal = valor
cedula = 50
totalcedula = 0
while True:
    if valortotal >= cedula:
        valortotal -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print("Sacando...")
            print(40 * "=")
            sleep(3)
            print(f"Total de {totalcedula} cédulas de R${cedula}.")
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if valortotal == 0:
            break
print(40 * "=")
print("{:^40}".format("SAQUE FINALIZADO"))
