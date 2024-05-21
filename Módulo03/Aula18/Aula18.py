"""teste = list()
teste.append("Kalleu")
teste.append(22)
galera = list()
galera.append(
    teste[:]
)  # Colocamos o [:] para fazer uma cópia da lista e não unir ambas
teste[0] = "Jorge"
teste[1] = 45
galera.append(teste[:])
print(galera)"""

'''galera = [["Jaozin", 14], ["Kalleu", 22], ["Jorgin", 30], ["Hannah Montanna", 140]]
"""print(galera[0])  # Busca a lista
print(galera[0][0])  # Busca o elemento dentro da lista
"""
for pessoa in galera:
    # print(pessoa)
    print(f"{pessoa[0]}, tem {pessoa[1]} anos.")'''

galera = list()
dado = list()
maior = menor = 0
for contagem in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        maior += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        menor += 1
print(f"Temos {maior} maiores de idade e {menor} menor.")
