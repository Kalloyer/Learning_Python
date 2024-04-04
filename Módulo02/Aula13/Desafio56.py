# Leia o nome, idade, sexo de 4 pessoas, no final mostre a média de idade do grupo, nome da pessoa mais velha, quantas mulheres tem menos de 20 anos
somaidade = 0
mediaidade = 0
idadehomemvelho = 0
nomevelho = 0
idademulhernova = 0
for p in range(1, 5):
    print(10 * "=", "{}ª Pessoa", 10 * "=")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M|F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in "Mm" and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in "Ff" and idade <= 20:
        idademulhernova += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos!".format(mediaidade))
print(
    "O homem mais velho do grupo tem {} anos, e seu nome é {}.".format(
        idadehomemvelho, nomevelho
    )
)
print("Ao todo são {} mulheres, com menos de 20 anos de idade.".format(idademulhernova))
