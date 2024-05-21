# Leia nome, sexo, idade de várias pessoas, guardando os dados em um dicionário e os dicionários em uma lista, mostre o total de pessoas cadastradas, a média de idade, uma lista com toas as mulheres, todas as pessoas acima da média de idade
pessoa = dict()
cadastros = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).lower().strip()[0]
        if pessoa["Sexo"] in "mf":
            break
        print("*ERROR* Digite apenas M ou F.")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    cadastros.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
        if resposta in "sn":
            break
        print("*ERROR* Digite apenas S ou N.")
    if resposta == "n":
        break
print(50 * "=")
print(f"Ao todos temos {len(cadastros)} pessoas cadastradas.")
media = soma / len(cadastros)
print(f"A média de idade é de {media:.0f} anos.")
print("As mulheres cadastradas foram: ", end="")
for mulher in cadastros:
    if mulher["Sexo"] == "f":
        print(f"[{mulher["Nome"]}]", end=" ")
print()
print("Lista das pessoas que estão acima da média: ")
for idade in cadastros:
    if idade["Idade"] >= media:
        print("  => ", end="")
        for chave, valor in idade.items():
            print(f"{chave} = {valor};", end=" ")
        print()
print(50 * "=")
print(f"{"PROGRAMA ENCERRADO":^50}")
