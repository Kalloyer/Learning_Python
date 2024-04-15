# Leia e idade e sexo de várias pessoas, a cada pessoa cadastrada, o programa deve perguntar se quer coninuar ou não, no final mostre quantas pessoas tem mais de 18 anos, quantas tem menos de 20, quantos homens foram cadastrados e quantas mulheres
contagem = demaior = homem = mulher = 0
while True:
    print(19 * "=")
    print("Cadastre uma Pessoa")
    print(19 * "=")
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "mf":
        sexo = str(input("Sexo [M/F]: ")).lower().strip()[0]
        if idade >= 18:
            demaior += 1
        if sexo == "m":
            homem += 1
        if sexo == "f" and idade < 20:
            mulher += 1
    continuar = " "
    while continuar not in "sn":
        print(19 * "=")
        continuar = input("Quer continuar? [S/N]: ").lower().strip()[0]
    if continuar == "n":
        print("=====Fim do Programa=====")
        break
print(f"Foram cadastradas {demaior} pessoas acima de 18 anos.")
print(f"Foram cadastrados {homem} homens.")
print(f"Foram cadastrados {mulher} mulheres com menos de 20 anos.")
