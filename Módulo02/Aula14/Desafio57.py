# Leia o sexo M ou F e se tiver errado peça para inserir o correto
sexo = str(input("Informe o seu sexo [M|F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = (
        str(input("Sexo digitado é inválido, digite novamente [M|F]: "))
        .strip()
        .upper()[0]
    )
print("Sexo {} digitado está correto!".format(sexo))
