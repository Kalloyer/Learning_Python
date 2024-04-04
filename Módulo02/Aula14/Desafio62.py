# Melhore o desafio 61 mostrando se o usuário quer mais temos
print(30 * "=")
print("     10 Termos de uma PA")
print(30 * "=")
valor = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
termo = valor
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print("{}".format(termo), end=" -> ")
        termo += razao
        contador += 1
    print("Esperando...")
    print(30 * "===")
    mais = int(input("Quantos termos você gostaria que mostrasse a mais? "))
print("Programa finalizado com {} termos exibidos em tela.".format(total))
