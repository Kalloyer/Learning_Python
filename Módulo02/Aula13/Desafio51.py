# Faça em PA do primeiro termo, com os 10 primeiros termos
print(30 * "=")
print("     10 Termos de uma PA")
print(30 * "=")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("Finalizado")
