# Refazer o desafio 51
print(30 * "=")
print("     10 Termos de uma PA")
print(30 * "=")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
primeiro = termo
contador = 1
while contador <= 10:
    print("{}".format(primeiro), end=" -> ")
    primeiro += razao
    contador += 1
print("Finalizado")
